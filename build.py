"""
Builds the Makwana's Studio legal site: one page set per game (policy + terms), plus a studio home page.

To change the company name, the contact email, the date or a game's wording:
edit the settings below, then run   python build.py   and commit the changed pages.
"""
import os
from html import escape

STUDIO = "Makwana's Studio"
EMAIL = 'bunnypanchal1432@gmail.com'  # shown publicly on every page: change it here, then rebuild
UPDATED = '3 November 2026'
BASE = 'https://makwanasstudio.github.io'

GAMES = [
    dict(
        slug='block-puzzle',
        name='MsS - Block Puzzle',
        tagline='Drag blocks onto the grid, clear rows and columns, and chase your best score.',
        stored=[
            'the player name you choose to type in (you can change it at any time);',
            'your best score for each play mode (Relaxing, Easy, Normal and Hard).',
        ],
        rewards='a hint, a shuffle of the pieces, or a second chance after a game over',
    ),
    dict(
        slug='arrow-puzzle',
        name='MsS - Arrow Puzzle',
        tagline='Tap each arrow to slide it out of the picture without hitting the others.',
        stored=[
            'the player name you choose to type in (you can change it at any time);',
            'the highest level you have reached, so you can continue where you left off.',
        ],
        rewards='a hint or an extra life',
    ),
    dict(
        slug='tile-puzzle',
        name='MsS - Tile Puzzle',
        tagline='Pick free tiles into the tray and match three to clear the board.',
        stored=[
            'the player name you choose to type in (you can change it at any time);',
            'the highest level you have reached in each tile category.',
        ],
        rewards='a hint, a shuffle, an undo, or a second chance when the tray is full',
    ),
    dict(
        slug='bottle-puzzle',
        name='MsS - Bottle Puzzle',
        tagline='Pour the liquids until every bottle holds just one colour.',
        stored=[
            'the player name you choose to type in (you can change it at any time);',
            'the highest level you have reached in each liquid theme.',
        ],
        rewards='a hint, an extra bottle, or an undo',
    ),
    dict(
        slug='button-puzzle',
        name='MsS - Button Puzzle',
        tagline='One button, one rule. Read carefully, press the right number of times, and do not get tricked.',
        stored=[
            'the player name you choose to type in (you can change it at any time);',
            'the language you choose (English, Hindi or Gujarati);',
            'the highest level you have reached and your last checkpoint, so you can continue where you left off.',
        ],
        rewards='a second chance on the same level or a look at the answer',
    ),
]

CSS = """:root { --bg:#120816; --panel:#2a1226; --text:#f3d9c4; --dim:#d9b8c4; --gold:#ffc857; --ember:#ff6b35; }
* { box-sizing: border-box; }
body { margin:0; font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  background: linear-gradient(180deg,#120816,#2b0f2e 60%,#1a0b14); background-attachment: fixed;
  color: var(--text); line-height: 1.65; min-height: 100vh; }
main { max-width: 760px; margin: 0 auto; padding: 32px 18px 64px; }
h1 { color: var(--gold); font-size: 1.9rem; margin: 0 0 4px; }
h2 { color: var(--ember); font-size: 1.2rem; margin-top: 30px; }
p, li { color: var(--text); }
.meta { color: var(--dim); font-size: .95rem; }
a { color: var(--gold); }
.card { background: var(--panel); border: 1px solid rgba(255,200,87,.35); border-radius: 14px; padding: 16px 18px; margin: 14px 0; }
.grid { display: grid; gap: 14px; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); margin-top: 18px; }
.nav { margin-bottom: 18px; font-size: .95rem; }
footer { margin-top: 40px; color: var(--dim); font-size: .9rem; }
"""


def page(title, body, depth):
    css = '../' * depth + 'assets/legal.css'
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<link rel="stylesheet" href="{css}">
</head>
<body>
<main>
{body}
<footer>&copy; 2026 {escape(STUDIO)}. All rights reserved.</footer>
</main>
</body>
</html>
"""


def nav(g, here):
    links = [('Home', f'{BASE}/'), (g['name'], f"{BASE}/{g['slug']}/"),
             ('Privacy Policy', f"{BASE}/{g['slug']}/privacy-policy.html"), ('Terms of Use', f"{BASE}/{g['slug']}/terms.html")]
    return '<p class="nav">' + ' &middot; '.join(f'<a href="{u}">{escape(t)}</a>' for t, u in links if t != here) + '</p>'


def privacy(g):
    stored = '\n    '.join(f'<li>{escape(x)}</li>' for x in g['stored'])
    n = escape(g['name'])
    body = f"""{nav(g, 'Privacy Policy')}
<h1>{n} &ndash; Privacy Policy</h1>
<p class="meta">Last updated: {UPDATED}</p>

<p>This policy explains what information the <strong>{n}</strong> mobile app (&ldquo;the app&rdquo;) handles when you play.
The app is published by <strong>{escape(STUDIO)}</strong> (&ldquo;we&rdquo;, &ldquo;us&rdquo;). In short:
<strong>we run no servers, you do not need an account, and we do not collect your personal information ourselves.</strong></p>

<h2>1. Information stored on your device</h2>
<p>The app saves the following only on your own phone, in the app&rsquo;s local storage:</p>
<ul>
    {stored}
</ul>
<p>This information is never sent to us or to any third party by the app. It is deleted when you uninstall the app or clear its storage.</p>

<h2>2. Advertising (Google AdMob)</h2>
<p>The app is free and is supported by ads from <strong>Google AdMob</strong>. You may see banner ads, full-screen ads between rounds,
and optional rewarded videos that you choose to watch in return for {escape(g['rewards'])}.</p>
<p>To show and measure ads, Google and its partners may collect and use information such as your device&rsquo;s advertising ID,
IP address, approximate location derived from the IP address, device and app information, and how you interact with ads.
Google does this under its own privacy policy and we do not receive this information. Learn more:
<a href="https://policies.google.com/technologies/partner-sites">How Google uses information from sites or apps that use its services</a> and the
<a href="https://policies.google.com/privacy">Google Privacy Policy</a>.</p>

<h2>3. Consent and your ad choices</h2>
<p>Where the law requires it (for example in the European Economic Area, the United Kingdom, Switzerland and some US states),
the app shows Google&rsquo;s consent form (Google User Messaging Platform) the first time you open it and before any ad is requested.
If you decline, ads are limited according to your choice.</p>
<p>You can review or change your choice at any time with the <strong>Ad Choices</strong> link on the app&rsquo;s start screen
(it is shown where the law requires it). You can also reset your advertising ID or opt out of personalised ads in your phone&rsquo;s settings
(Android: Settings &rarr; Privacy &rarr; Ads).</p>

<h2>4. Information we do not collect</h2>
<ul>
    <li>We do not ask for or store your email address, phone number, contacts, photos or files.</li>
    <li>We do not collect precise location, and the app does not use your camera or microphone.</li>
    <li>We do not use analytics or tracking tools of our own, and we do not sell your data.</li>
</ul>

<h2>5. Children</h2>
<p>The app is intended for a general audience and is not directed to children under 13. We do not knowingly collect personal
information from children. If you believe a child has given us personal information, contact us and we will help.</p>

<h2>6. Data retention and deletion</h2>
<p>Because we hold no personal data on any server, there is nothing for us to delete. All app data lives on your device and is removed
when you clear the app&rsquo;s storage or uninstall it. There is no account to close.</p>

<h2>7. Your rights</h2>
<p>Depending on where you live (for example under the GDPR, UK GDPR or California privacy law), you may have rights to access, correct,
delete or object to the use of your personal data. We hold none about you; for data used by Google to show ads, use your Google account&rsquo;s
ad settings. You can contact us with any question.</p>

<h2>8. Security</h2>
<p>The app does not transmit your saved name or progress anywhere. Ads are delivered over secure connections by Google&rsquo;s ad SDK.</p>

<h2>9. Changes to this policy</h2>
<p>We may update this policy from time to time. The date at the top shows when it last changed.
Continuing to use the app after an update means you accept the updated policy.</p>

<h2>10. Contact us</h2>
<div class="card"><p style="margin:0">Questions about this policy? Email <strong>{escape(STUDIO)}</strong> at
<a href="mailto:{escape(EMAIL)}">{escape(EMAIL)}</a>.</p></div>
"""
    return page(f"{g['name']} - Privacy Policy", body, 1)


def terms(g):
    n = escape(g['name'])
    body = f"""{nav(g, 'Terms of Use')}
<h1>{n} &ndash; Terms of Use</h1>
<p class="meta">Last updated: {UPDATED}</p>

<p>These terms apply to your use of the <strong>{n}</strong> mobile app (&ldquo;the app&rdquo;), published by
<strong>{escape(STUDIO)}</strong>. By installing or playing the app you agree to them.</p>

<h2>1. Licence</h2>
<p>We give you a personal, non-exclusive, non-transferable licence to install and play the app on your own devices for entertainment.
You may not copy, modify, sell, rent, reverse-engineer or redistribute the app or any part of it.</p>

<h2>2. Ads and rewards</h2>
<p>The app is free and shows ads. Rewarded videos are always optional. Rewards (such as hints or extra chances) exist only inside the game,
have no cash value and cannot be exchanged. See the <a href="{BASE}/{g['slug']}/privacy-policy.html">Privacy Policy</a> for how ads and consent work.</p>

<h2>3. Your progress</h2>
<p>Your name and progress are saved only on your device. If you uninstall the app, clear its data or change phones, they may be lost.</p>

<h2>4. Ownership</h2>
<p>The app, including its code, artwork, music and sound effects, belongs to {escape(STUDIO)} and is protected by copyright.</p>

<h2>5. No warranty</h2>
<p>The app is provided &ldquo;as is&rdquo;, without promises that it will be error-free or always available. To the extent the law allows,
{escape(STUDIO)} is not liable for any loss arising from your use of the app.</p>

<h2>6. Changes</h2>
<p>We may update the app or these terms. The date above shows the latest version. If you do not agree with a change, stop using the app.</p>

<h2>7. Contact</h2>
<div class="card"><p style="margin:0">Questions? Email <a href="mailto:{escape(EMAIL)}">{escape(EMAIL)}</a>.</p></div>
"""
    return page(f"{g['name']} - Terms of Use", body, 1)


def game_home(g):
    n = escape(g['name'])
    body = f"""{nav(g, g['name'])}
<h1>{n}</h1>
<p>{escape(g['tagline'])}</p>
<div class="card">
<p style="margin:0 0 6px"><a href="{BASE}/{g['slug']}/privacy-policy.html">Privacy Policy</a></p>
<p style="margin:0"><a href="{BASE}/{g['slug']}/terms.html">Terms of Use</a></p>
</div>
<p class="meta">Published by {escape(STUDIO)}. Contact: <a href="mailto:{escape(EMAIL)}">{escape(EMAIL)}</a></p>
"""
    return page(g['name'], body, 1)


def studio_home():
    cards = '\n'.join(
        f"""<div class="card"><h2 style="margin-top:0"><a href="{BASE}/{g['slug']}/">{escape(g['name'])}</a></h2>
<p style="margin:0 0 8px">{escape(g['tagline'])}</p>
<p style="margin:0" class="meta"><a href="{BASE}/{g['slug']}/privacy-policy.html">Privacy Policy</a> &middot;
<a href="{BASE}/{g['slug']}/terms.html">Terms of Use</a></p></div>"""
        for g in GAMES
    )
    body = f"""<h1>{escape(STUDIO)}</h1>
<p>Casual puzzle games. Pick a game to read its privacy policy and terms.</p>
<div class="grid">
{cards}
</div>
<p class="meta">Contact: <a href="mailto:{escape(EMAIL)}">{escape(EMAIL)}</a></p>
"""
    return page(STUDIO, body, 0)


def write(path, text):
    os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    write(os.path.join(here, 'assets', 'legal.css'), CSS)
    write(os.path.join(here, '.nojekyll'), '')
    write(os.path.join(here, 'index.html'), studio_home())
    for g in GAMES:
        write(os.path.join(here, g['slug'], 'index.html'), game_home(g))
        write(os.path.join(here, g['slug'], 'privacy-policy.html'), privacy(g))
        write(os.path.join(here, g['slug'], 'terms.html'), terms(g))
    print('built', len(GAMES), 'games')
    for g in GAMES:
        print(f"  {g['name']}: {BASE}/{g['slug']}/privacy-policy.html")
