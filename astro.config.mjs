// @ts-check

import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import cloudflare from '@astrojs/cloudflare';
import { defineConfig } from 'astro/config';
import mermaid from 'astro-mermaid';

// https://astro.build/config
export default defineConfig({
  site: 'https://maswahyu.biz.id',
  output: 'static',
  integrations: [mdx(), sitemap(), mermaid()],

  image: {
      // Use static image service for Cloudflare Pages
      service: {
          entrypoint: 'astro/assets/services/sharp',
          config: {
              limitInputPixels: false,
          },
      },
	},

  adapter: cloudflare(),
});