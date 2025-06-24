import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "zFont",
  description: "Android Emoji & Font Changer",
  head: [
    ['link', { rel: 'icon', href: 'icons/favicon.ico' }],
    [
      'meta',
      {
        name: 'theme-color',
        content: '#00A052'
      }
    ],
    [
      'link',
      {
        ref: 'manifest',
        href: 'manifest.json'
      }
    ],
    [
      'link',
      {
        ref: 'apple-touch-icon',
        href: 'icons/icon-192.png'
      }
    ],
    // Meta keywords (not widely used in modern SEO but can still help)
    [
      'meta',
      {
        name: 'keywords',
        content: 'Android font changer, iOS Emoji Android, Samsung iOS Emoji, Vivo iOS Emoji, Oppo iOS Emoji, iOS Emoji, Oppo iPhone Emoji, iPhone Emoji, Custom emoji app, Change Android fonts, No root font changer, zFont app download, Android text style customization, Free Android font installer, Mobile typography changer, Emoji customization Android, System font modifier, Android personalization app, Custom phone fonts, Android text appearance, Stylish fonts for Android, Phone emoji customizer, Android font style app, zFont no root, Typography customization app, Android font library, Smartphone font installer, Font style without root, Custom Android typography, Phone text customizer, Android font manager, Cool fonts for Android, Font pack installer, Samsung font changer, Change system font Android, Express with fonts, Personalize Android look, Device font switcher, Best font changer app, Unicode font support, Font preview app, Xiaomi font installer, Android UI customization, Font size changer, Emoji replacer Android, Font collection app, Modern phone fonts'
      }
    ],
    // Open Graph tags for better social media sharing
    [
      'meta',
      {
        property: 'og:title',
        content: 'zFont - Android Emoji & Font Changer'
      }
    ],
    [
      'meta',
      {
        property: 'og:description',
        content: '✅ Android Font changer for Samsung, Vivo, OnePlus, ASUS, LG, OPPO, Huawei, Honor, Realme, Tecno, and Infinix 🎉'
      }
    ],
    [
      'meta',
      {
        property: 'og:image',
        content: 'https://zfont.app/icons/play_store_feature_graphic.png'
      }
    ],
    [
      'meta',
      {
        property: 'og:url',
        content: 'https://zfont.app'
      }
    ],
  ],
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    logo: '/icons/icon-192.png',
    nav: [
      { text: 'Home', link: '/' },
      {text: "Help", link: "/help"},
      {
        text: 'About',
        items: [
          {text: 'zFile', link: '/zfile'},
          { text: 'Privacy Policy', link: '/privacy' },
          { text: 'Terms and Conditions', link: '/terms' },
        ]
      }
    ],

    sidebar: [
      {
        text: "Help", 
        items: [
          {text: 'FAQ', link: '/help'},
          {text: 'Contact & Support', link: '/contact'},
        ]
      },
      {
        text: 'About',
        items: [
          {text: 'zFile', link: '/zfile'},
          { text: 'Privacy Policy', link: '/privacy' },
          { text: 'Terms and Conditions', link: '/terms' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'googleplay', link: 'https://play.google.com/store/apps/details?id=com.htetznaing.zfont2' },
      { icon: 'facebook', link: 'https://www.facebook.com/zFontApp' },
      { icon: 'telegram', link: 'https://t.me/zFontApp' },
      { icon: 'github', link: 'https://github.com/zFont' },
    ],
    footer: {
      message: "&lt;Made with 💚 from Myanmar/&gt;",
      copyright: 'Copyright © 2019-Present Khun Htetz Naing'
    }
  }
})
