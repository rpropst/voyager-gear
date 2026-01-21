# CORS Configuration Guide

## Current Configuration

The Voyager Gear API is now configured with proper CORS support for development and production environments.

## CORS Settings

### Allowed Origins (Development)
- `http://localhost:3000`
- `http://127.0.0.1:3000`
- `http://localhost:5173`
- `http://127.0.0.1:5173`
- `http://localhost:5174`
- `http://127.0.0.1:5174`

### CORS Middleware Settings
- **Allow Credentials**: `true` (enables cookies and authorization headers)
- **Allow Methods**: `GET, POST, PUT, DELETE, OPTIONS, PATCH`
- **Allow Headers**: `*` (all headers)
- **Expose Headers**: `*` (all response headers)
- **Max Age**: `3600` seconds (1 hour preflight cache)

## Quick Start

### 1. Start Backend Server
```bash
cd backend
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate     # On Windows

python run.py
```

Server runs on: **http://localhost:5001**

### 2. Start Frontend
```bash
cd frontend
npm run dev
```

Frontend typically runs on: **http://localhost:3000** or **http://localhost:5173**

### 3. Verify CORS is Working

Open your browser's Developer Tools (F12) and check the Console tab. You should see:
- ✅ No CORS errors
- ✅ API requests completing successfully
- ✅ Products loading correctly

## Testing CORS

### Using Browser Console
```javascript
// Test from browser console
fetch('http://localhost:5001/api/products')
  .then(res => res.json())
  .then(data => console.log('Products:', data))
  .catch(err => console.error('Error:', err));
```

### Using curl
```bash
# Test basic request
curl -i http://localhost:5001/api/products

# Test with Origin header (simulates browser request)
curl -i -H "Origin: http://localhost:3000" \
     -H "Access-Control-Request-Method: GET" \
     http://localhost:5001/api/products

# Test preflight OPTIONS request
curl -i -X OPTIONS \
     -H "Origin: http://localhost:3000" \
     -H "Access-Control-Request-Method: POST" \
     -H "Access-Control-Request-Headers: Content-Type,Authorization" \
     http://localhost:5001/api/products
```

## Customizing CORS Origins

### Option 1: Environment Variable (Recommended)

Create a `.env` file in the `backend` directory:

```env
CORS_ORIGINS=http://localhost:3000,http://localhost:5173,https://yourdomain.com
```

### Option 2: Direct Configuration

Edit `backend/app/config.py`:

```python
CORS_ORIGINS: str = "http://localhost:3000,http://localhost:5173"
```

**Note**: After changing CORS settings, restart the backend server.

## Common Issues and Solutions

### Issue: CORS Error "No 'Access-Control-Allow-Origin' header"

**Symptoms:**
```
Access to fetch at 'http://localhost:5001/api/products' from origin 'http://localhost:3000' 
has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present
```

**Solutions:**
1. Verify backend server is running on port 5001
2. Check that your frontend origin is in the CORS_ORIGINS list
3. Restart the backend server after configuration changes

### Issue: "Credentials flag is 'true', but the 'Access-Control-Allow-Origin' header is '*'"

**Symptoms:**
```
Access to fetch has been blocked by CORS policy: The value of the 'Access-Control-Allow-Origin' 
header in the response must not be the wildcard '*' when the request's credentials mode is 'include'
```

**Solution:**
✅ Already fixed! We use specific origins instead of wildcard.

### Issue: Preflight OPTIONS Request Failing

**Symptoms:**
- OPTIONS requests return 404 or 405
- Requests work in Postman but not in browser

**Solution:**
✅ Already fixed! FastAPI automatically handles OPTIONS requests with our CORS middleware.

### Issue: Different Port Than Expected

**Symptoms:**
- Frontend runs on port 5174 instead of 3000
- CORS error for unexpected port

**Solution:**
Add the port to CORS_ORIGINS:
```env
CORS_ORIGINS=http://localhost:3000,http://localhost:5173,http://localhost:5174
```

## Production Deployment

### Security Checklist

- [ ] Set `DEBUG=False`
- [ ] Set `ENVIRONMENT=production`
- [ ] Use HTTPS for all origins
- [ ] Specify exact production domain(s)
- [ ] Remove development origins (localhost)
- [ ] Use strong SECRET_KEY
- [ ] Enable rate limiting
- [ ] Use PostgreSQL instead of SQLite

### Production .env Example

```env
# Application
DEBUG=False
ENVIRONMENT=production

# Server
HOST=0.0.0.0
PORT=5001

# Database
DATABASE_URL=postgresql://user:password@localhost/voyager_gear

# JWT
SECRET_KEY=your-production-secret-key-here-use-openssl-rand-hex-32
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS - Production domains only
CORS_ORIGINS=https://yourdomain.com,https://www.yourdomain.com

# Rate Limiting
RATE_LIMIT_PER_MINUTE=60
AUTH_RATE_LIMIT_PER_MINUTE=5
```

## Architecture

### How CORS Works

1. **Simple Requests**: Browser sends request with `Origin` header
2. **Server Response**: Includes `Access-Control-Allow-Origin` header
3. **Preflight Requests**: For complex requests (POST, custom headers)
   - Browser sends OPTIONS request first
   - Server responds with allowed methods/headers
   - Browser sends actual request if approved

### Our Implementation

```python
# backend/app/main.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,  # Specific origins
    allow_credentials=True,                     # Allow cookies/auth
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["*"],                        # All request headers
    expose_headers=["*"],                       # All response headers
    max_age=3600,                              # Cache preflight 1 hour
)
```

## Debugging Tips

### 1. Check Response Headers

In browser DevTools Network tab, look for these headers in the response:
```
access-control-allow-origin: http://localhost:3000
access-control-allow-credentials: true
access-control-expose-headers: *
```

### 2. Check Request Headers

The browser automatically adds:
```
origin: http://localhost:3000
```

### 3. Enable Verbose Logging

In `backend/run.py`, the server runs with `log_level="info"` which shows all requests.

### 4. Test Without CORS

Use a tool like Postman or curl to verify the API works (these don't enforce CORS).

## Additional Resources

- [MDN CORS Documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
- [FastAPI CORS Middleware](https://fastapi.tiangolo.com/tutorial/cors/)
- [Starlette CORS Middleware](https://www.starlette.io/middleware/#corsmiddleware)

## Support

If you continue to experience CORS issues:

1. Check the browser console for specific error messages
2. Verify both frontend and backend are running
3. Confirm the frontend is using the correct API URL
4. Check that your origin is in the CORS_ORIGINS list
5. Restart both frontend and backend servers

## Files Modified

- `backend/app/main.py` - CORS middleware configuration
- `backend/app/config.py` - CORS origins settings
- `backend/README.md` - Added troubleshooting section
