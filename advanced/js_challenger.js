const puppeteer = require('puppeteer');

(async () => {
    const targetURL = process.argv[2];

    if (!targetURL) {
        console.log("🔴 Provide a target URL: node js_challenger.js https://target.com");
        process.exit();
    }

    console.log(`⚔️ Launching browser to bypass protection: ${targetURL}`);

    const browser = await puppeteer.launch({ headless: true });
    const page = await browser.newPage();

    page.on('response', response => {
        if (response.status() === 403 || response.status() === 429) {
            console.log(`🔒 Bypass Failed: ${response.status()} - ${response.url()}`);
        }
    });

    try {
        await page.goto(targetURL, { waitUntil: 'networkidle2', timeout: 30000 });
        console.log("✅ JS Challenge Passed. Page Title:", await page.title());
    } catch (error) {
        console.log("❌ Error bypassing protection:", error.message);
    }

    await browser.close();
})();
