# E-Cell SMEC Website

Official website for E-Cell SMEC - The Entrepreneurship Cell of St. Martin's Engineering College.

## 🚀 Features

- **Responsive Design**: Optimized for all devices (mobile, tablet, desktop)
- **Modern UI**: Built with Tailwind CSS and modern design principles
- **SEO Optimized**: Complete meta tags, sitemap, and structured data
- **Performance**: Lazy loading, compression, and caching optimizations
- **Accessibility**: WCAG compliant with proper focus management
- **PWA Ready**: Web app manifest for mobile app-like experience
- **Security**: Security headers and CSP implementation

## 📱 Pages

- **Homepage** (`index.html`) - Main landing page with hero, about, team, events, and blog sections
- **Blog** (`blog.html`) - All blog posts with filtering and search
- **Events** (`events.html`) - Overview of all events
- **Illuminate Event** (`illuminate-event.html`) - Dedicated page for Illuminate event
- **Eureka Event** (`ekkuvba-event.html`) - Dedicated page for Eureka event
- **404 Error** (`404.html`) - Custom error page

## 🛠️ Development

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/ecell-smec/website.git
cd website
```

2. Start local server:
```bash
python3 -m http.server 8000
```

3. Open browser: `http://localhost:8000`

### File Structure

```
├── index.html              # Homepage
├── blog.html               # Blog listing page
├── events.html             # Events overview
├── illuminate-event.html   # Illuminate event page
├── ekkuvba-event.html      # Eureka event page
├── 404.html                # Error page
├── robots.txt              # SEO robots file
├── sitemap.xml             # SEO sitemap
├── site.webmanifest        # PWA manifest
├── .htaccess               # Apache configuration
├── package.json            # Project metadata
├── README.md               # This file
├── blog/                   # Blog images
├── eureka/                 # Eureka event images
├── illuminate event/       # Illuminate event images
└── lovable-uploads/        # Team member images
```

## 🚀 Deployment

### Option 1: Static Hosting (Recommended)

**Netlify:**
1. Connect your GitHub repository to Netlify
2. Set build command: `echo "Static site"`
3. Set publish directory: `/`
4. Deploy!

**Vercel:**
1. Import project from GitHub
2. Framework preset: Other
3. Deploy!

**GitHub Pages:**
1. Enable GitHub Pages in repository settings
2. Source: Deploy from a branch
3. Branch: main
4. Save!

### Option 2: Traditional Web Hosting

1. Upload all files to your web server
2. Ensure `.htaccess` is supported (Apache)
3. Configure SSL certificate
4. Update DNS records

### Option 3: CDN Deployment

**Cloudflare:**
1. Add your domain to Cloudflare
2. Upload files via Cloudflare Pages
3. Configure custom domain

## 🔧 Configuration

### Google Analytics

Replace `GA_MEASUREMENT_ID` in `index.html` with your actual Google Analytics ID:

```html
<script async src="https://www.googletagmanager.com/gtag/js?id=YOUR_GA_ID"></script>
```

### Domain Configuration

Update the following files with your actual domain:

- `index.html` - Update canonical URLs and Open Graph URLs
- `sitemap.xml` - Update all URLs
- `robots.txt` - Update sitemap URL

### Favicon

Add your favicon files to the root directory:
- `favicon.ico`
- `favicon-16x16.png`
- `favicon-32x32.png`
- `apple-touch-icon.png`
- `android-chrome-192x192.png`
- `android-chrome-512x512.png`

## 📊 Performance

The website is optimized for performance with:

- **Lazy Loading**: Images load only when needed
- **Compression**: Gzip compression enabled
- **Caching**: Browser caching for static assets
- **Minification**: Optimized CSS and JavaScript
- **CDN Ready**: Compatible with CDN deployment

## 🔒 Security

Security features implemented:

- **Security Headers**: XSS protection, content type options
- **CSP**: Content Security Policy
- **HTTPS Ready**: SSL/TLS configuration
- **Input Validation**: Form validation and sanitization

## 📱 Mobile Optimization

- **Responsive Design**: Works on all screen sizes
- **Touch Friendly**: Optimized for touch interactions
- **Fast Loading**: Optimized for mobile networks
- **PWA Ready**: Can be installed as mobile app

## 🎨 Customization

### Colors

Primary color is defined in Tailwind config:
```javascript
colors: {
    primary: "#f9bc06", // Yellow
    "background-light": "#f8f8f5",
    "background-dark": "#231e0f",
}
```

### Fonts

Using Plus Jakarta Sans font family for modern typography.

## 📞 Support

For support or questions:
- Email: ecell@smec.ac.in
- GitHub Issues: [Create an issue](https://github.com/ecell-smec/website/issues)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

**Made with ❤️ by E-Cell SMEC Team**
