import { ProxyAgent, setGlobalDispatcher } from 'undici';

const proxyUrl = process.env.HTTPS_PROXY || process.env.HTTP_PROXY;

if (proxyUrl) {
    const proxyAgent = new ProxyAgent(proxyUrl);
    setGlobalDispatcher(proxyAgent);
    console.log('[DEBUG] Global dispatcher set with proxy:', proxyUrl);
} else {
    console.log('[DEBUG] No proxy environment variable set. Global dispatcher not modified.');
}