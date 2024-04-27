module.exports = {
    async rewrites() {
      return {
        beforeFiles: [
          // These rewrites are checked before files and pages in the `public` folder
        ],
        afterFiles: [
          // These rewrites are checked after pages have been checked
          {
            source: '/api/:path*',
            destination: 'http://127.0.0.1:5328/:path*', // Proxy to Backend
          },
        ],
        fallback: [
          // These rewrites are checked after both `beforeFiles` and `afterFiles`, but before 404 logic
        ],
      };
    },
    images: {
      domains: ['racquetguys.ca', 'tadssportinggoods.ca', 'www.merchantoftennis.com']
    },
    // Your other Next.js configurations...
  };
  