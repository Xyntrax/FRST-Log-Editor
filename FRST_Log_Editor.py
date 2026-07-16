import os
import sys
import datetime
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# clean and important
CLEAN_STRINGS = {
    "14EC5FE4-5B1E-42B9-9EDA-F281C1506E7A",
    "89B4C1CD-B018-4511-B0A1-5476DBF70820",
    "8203C095-FB62-4005-807D-7C9A3775D1EA",
    "Edge DefaultProfile: Default",
    "Edge Extension: (uBlock Origin)",
    "Edge Extension: (HTTPS Everywhere)",
    "Edge Extension: (Kaspersky Protection)",
    "Edge Extension: (Malwarebytes Browser Guard)",
    "Edge Extension: (Outlook)",
    "Edge Extension: (Word)",
    "Edge Extension: (Excel)",
    "Edge Extension: (PowerPoint)",
    "Edge Extension: (IDM Integration Module)",
    "Edge Extension: (Bitdefender Anti-tracker)",
    "FF Extension: (Avast Online Security)",
    "FF Extension: (Avast SafePrice | Comparison, deals, coupons)",
    "FF Extension: (Adblock Plus - free ad blocker)",
    "FF Extension: (uBlock Origin)",
    "FF Extension: (Adobe Acrobat)",
    "FF Extension: (Bitdefender Wallet)",
    "FF Extension: (Bitdefender Anti-tracker)",
    "FF Extension: (Bitdefender Antispam Toolbar)",
    "FF Extension: (IDM integration)",
    "FF Extension: (IDM CC)",
    "BRA Extension: (Malwarebytes Browser Guard)",
    "BRA Extension: (IDM Integration Module)",
    "BRA Extension: (Brave Local Data Files Updater)",
    "BRA Extension: (Brave Ad Block Updater (Default))",
    "BRA Extension: (Brave NTP sponsored images)",
    "BRA Extension: (Brave SpeedReader Updater)",
    "BRA Extension: (Brave HTTPS Everywhere Updater)",
    "OPR Extension: (Rich Hints Agent)",
    "OPR Extension: (Amazon Assistant Promotion)",
    "CHR Extension: (Google Drive)",
    "CHR Extension: (YouTube)",
    "CHR Extension: (uBlock Origin)",
    "CHR Extension: (HTTPS Everywhere)",
    "CHR Extension: (Chrome Web Store Payments)",
    "CHR Extension: (Gmail)",
    "CHR Extension: (Chrome Media Router)",
    "CHR Extension: (Slides)",
    "CHR Extension: (Docs)",
    "CHR Extension: (Sheets)",
    "CHR Extension: (Google Docs Offline)",
    "CHR Extension: (Kaspersky Protection)",
    "CHR Extension: (Grammarly for Chrome)",
    "CHR Extension: (Duolingo on the Web)",
    "CHR Extension: (Avast Online Security)",
    "CHR Extension: (Avast SafePrice | Comparison, deals, coupons)",
    "CHR Extension: (Adobe Acrobat)",
    "CHR Extension: (Malwarebytes Browser Guard)",
    "CHR Extension: (Emsisoft Browser Security)",
    "CHR Extension: (Decentraleyes)",
    "CHR Extension: (LocalCDN)",
    "CHR Extension: (User-Agent Switcher for Chrome)",
    "CHR Extension: (Quick source viewer)",
    "CHR Extension: (Decentraleyes)",
    "CHR Extension: (Tampermonkey)",
    "CHR Extension: (Dark Reader)",
    "CHR Extension: (IDM Integration Module)",
    "CHR Extension: (EditThisCookie)",
    "CHR Extension: (Cookie-Editor)",
    "CHR Extension: (BetterTTV)",
    "CHR Extension: (ColorPick Eyedropper)",
    "CHR Extension: (Proxy SwitchyOmega)",
    "CHR Extension: (Sci-Hub X Now!)",
    "CHR Extension: (Bypass Paywalls Clean)",
    "CHR Extension: (Untrusted Types for DevTools)",
    "CHR Extension: (Adblock Plus - free ad blocker)",
    "CHR Extension: (Privacy Badger)",
    "CHR Extension: (Google Translate)",
    "CHR Extension: (Adobe Acrobat: PDF edit, convert, sign tools)",
    "BRA Extension: (Wallet Data Files Updater)",
    "bojobppfploabceghnmlahpoonbcbacn", # Malwarebytes Browser Guard (edge)
    "jmjflgjpcpepeafmmgdpfkogkghcpiha", # Edge relevant text changes (edge)
    "aeblfdkhhhdcdjpifhhbdiojplfjncoa", # 1Password – Password Manager (chromium)
    "ihcjicgdanjaechkgeegckofjjedodee", # Malwarebytes Browser Guard (chromium)
    "ghbmnnjooekpmoecnnnilnnbdlolhkhi", # Google Docs Offline (chromium)
    "gighmmpiobklfepjocnamgkkbiglidom", # AdBlock — block ads across the web (chromium)
    "mmioliijnhnoblpgimnlajmefafdfilb", # Shazam: Find song names from your browser (chromium)
    "ponfpcnoihfmfllpaingbgckeeldkhle", # Enhancer for YouTube™ (chromium)
    "nkbihfbeogaeaoehlefnkodbefgpgknn", # MetaMask (chromium)
    "amaaokahonnfjjemodnpmeenfpnnbkco", # Grepper (chromium)
    "bcjindcccaagfpapjjmafapmmgkkhgoa", # JSON Formatter (chromium)
    "fbgcedjacmlbgleddnoacbnijgmiolem", # Microsoft Bing Search with Rewards (chromium)
    "gngocbkfmikdgphklgmmehbjjlfgdemm", # SwagButton (chromium)
    "pocpnlppkickgojjlmhdmidojbmbodfm", # Chromebook Recovery Utility (chromium)
    "R2 NVDisplay.ContainerLocalSystem;",
    "(2BrightSparks Pte Ltd )",
    "(Adobe Systems)",
    "(Audyssey Labs)",
    "(Broadcom)",
    "(Conexant Systems Inc.)",
    "(DTS)",
    "(DTS, Inc.)",
    "(Digimarc)",
    "(Discord Inc.)",
    "(Dolby Laboratories)",
    "(Dolby Laboratories, Inc.)",
    "(EldoS Corporation)",
    "(Farbar)",
    "(General Workings, Inc.)",
    "(Harman)",
    "(ICEpower a/s)",
    "(Igor Pavlov)",
    "(Initex)",
    "(Intel)",
    "(Khronos Group)",
    "(Mente Binária)",
    "(MicroWorld Technologies Inc.)",
    "(Mozilla Foundation)",
    "(Mozilla)",
    "(Oracle Corporation)",
    "(Other World Computing, Inc.)",
    "(Pango Inc)",
    "(Razer Inc)",
    "(Real Sound Lab SIA)",
    "(Realtek semiconductor)",
    "(SRS Labs, Inc.)",
    "(Seiko Epson Corporation)",
    "(Skype)",
    "(Sony Corporation)",
    "(Sound Research, Corp.)",
    "(Synopsys, Inc.)",
    "(Sysinternals - www.sysinternals.com)",
    "(TOSHIBA CORPORATION.)",
    "(TOSHIBA Corporation)",
    "(The ICU Project)",
    "(Tonec Inc.)",
    "(Toshiba Client Solutions Co., Ltd.)",
    "(VSO Software)",
    "(Virage Logic Corporation / Sonic Focus)",
    "(VoodooSoft, LLC)",
    "(Windows (R) Win 7 DDK provider)",
    "(Yamaha Corporation)",
    "(curl, hxxps://curl.se/)",
    "(Electronic Arts)",
    "(On2.com)",
    "(Logitech)",
    "(Tonec Inc.)",
    "2BrightSparks Pte. Ltd.",
    "A-Volute SAS",
    "A-Volute",
    "ARCAI",
    "ASROCK Incorporation",
    "ASUSTEK COMPUTER INC.",
    "ASUSTeK Computer Inc.",
    "AVB Disc Soft, SIA",
    "Acer Incorporated",
    "Acro Software Inc.",
    "Adobe Inc.",
    "Adobe Systems Incorporated",
    "Adobe Systems, Incorporated",
    "Advanced Micro Devices Inc.",
    "Advanced Micro Devices, Inc",
    "Advanced Micro Devices, Inc.",
    "Amazon.com Services LLC",
    "AnchorFree Inc",
    "Apple Inc.",
    "Autodesk, Inc.",
    "Avid Technology, Inc.",
    "BattlEye Innovations e.K.",
    "Beijing NormalSoft technology Co.,Ltd.",
    "Blizzard Entertainment, Inc.",
    "Bluestack Systems, Inc",
    "CPUID S.A.R.L.U.",
    "Canon Inc.",
    "Citrix Systems, Inc.",
    "Code Sector",
    "Conexant Systems, Inc.",
    "Corel Corporation",
    "Corsair Memory, Inc.",
    "Dell Inc",
    "Digiarty Software, Inc.",
    "Disc Soft Ltd",
    "Discord Inc.",
    "Dolby Laboratories, Inc.",
    "Dropbox, Inc",
    "ELAN Microelectronics Corp.",
    "EVGA Co., Ltd.",
    "EVGA Corp.",
    "EasyAntiCheat Oy",
    "EldoS Corporation",
    "Electronic Arts, Inc.",
    "Epic Games Inc.",
    "Even Balance, Inc.",
    "Figma, Inc.",
    "Flexera Software LLC",
    "Fortemedia Inc",
    "GIGA-BYTE TECHNOLOGY CO., LTD.",
    "Gaijin Network LTD",
    "Gemalto, Inc.",
    "Glarysoft LTD",
    "Global Media (Thailand) Co., Ltd",
    "GoTrustID Inc.",
    "Google Inc.",
    "Google LLC",
    "Guillaume Ryder (hxxp://utilfr42.free.fr)",
    "HP Inc.",
    "Hewlett Packard",
    "Hewlett-Packard Co.",
    "Hewlett-Packard Company",
    "Huawei Technologies Co., Ltd.",
    "INTEL CORP",
    "Initeks, OOO",
    "Initex",
    "Insecure.Com LLC",
    "Intel Corporation",
    "Intel(R) Corporation",
    "Intel(R) pGFX",
    "Ivaylo Beltchev",
    "Kilonova LLC",
    "Kristjan Skutta",
    "Lenovo (Beijing) Limited",
    "Lenovo",
    "Lenovo.",
    "LogMeIn, Inc.",
    "Logitech, Inc.",
    "MICRO-STAR INTERNATIONAL CO., LTD",
    "MICRO-STAR INTERNATIONAL CO., LTD.",
    "MICSYS Technology Co., Ltd.",
    "Mediafour Corporation",
    "Micro-Star International CO., LTD.",
    "Microsemi Corporation.",
    "Microsemi Storage Solutions Inc.",
    "Microsoft Corp.",
    "Microsoft Corporation",
    "Microsoft Windows",
    "MiniTool Solution Ltd",
    "Mozilla Corporation",
    "NVIDIA Corporation",
    "Node.js Foundation",
    "Notepad++",
    "Nuance Communications, Inc.",
    "OOO Lightshot",
    "Open Source Developer, Dominik Reichl",
    "OpenJS Foundation",
    "Oracle America, Inc.",
    "Other World Computing, Inc",
    "PACE Anti-Piracy, Inc.",
    "PC Micro Systems Inc.",
    "Pango Inc.",
    "Parsec Cloud, Inc.",
    "Piriform Software Ltd",
    "Primera Technology, Inc.",
    "QFX Software Corporation",
    "Qualcomm Atheros",
    "RealNetworks, Inc.",
    "Realtek Semiconductor Corp",
    "Realtek Semiconductor Corp.",
    "Red Giant Software LLC",
    "Riot Games, Inc.",
    "Riverbed Technology, Inc.",
    "Rivet Networks LLC",
    "Rockstar Games, Inc.",
    "SCREENOVATE TECHNOLOGIES LTD.",
    "SEIKO EPSON CORPORATION",
    "SEIKO EPSON Corporation",
    "Samsung Electronics CO., LTD.",
    "Samsung Electronics Co., Ltd.",
    "SanDisk Corporation",
    "Shaul Eizikovich",
    "Skype Software Sarl",
    "Smart Sound Technology",
    "SonicWall Inc.",
    "Sony Imaging Products & Solutions Inc.",
    "Sound Research Corporation",
    "Spotify AB",
    "SteelSeries ApS",
    "Sublime HQ Pty Ltd",
    "SurfRight B.V.",
    "Swift Media Entertainment, Inc.",
    "Symantec Corporation",
    "Synaptics Incorporated",
    "TEFINCOM S.A.",
    "TeamViewer Germany GmbH",
    "Threatstar B.V.",
    "Tonalio GmbH",
    "Tonec Inc.",
    "Travis Lee Robinson",
    "Valve Corp.",
    "Valve Corporation",
    "VideoLAN",
    "Wacom Co., Ltd.",
    "Wacom Technology Corp.",
    "Wacom Technology, Corp.",
    "Waves Inc",
    "Western Digital Technologies, Inc.",
    "Wondershare Technology Co.,Ltd",
    "X-Rite Incorporated",
    "magicJack, L.P.",
    "voidtools",
    "Mega Limited",
    "Shenzhen Evision Semiconductor Technology Co., Ltd",
    "Shenzhen Evision Semiconductor Technology Co.,Ltd.",
    "Shanghai Yitu Information Technology Co.,Ltd.",
    "e2eSoft",
    "PUBG CORPORATION",
    "Int3 Software AB",
    "Giga-Byte Technology",
    "Windows (R) Server 2003 DDK provider",
    "VMware, Inc.",
    "Firebit OU",
    "Rainmeter",
    "kernel-panik",
    "Razer USA Ltd.",
    "The CefSharp Authors",
    "Razer Inc.",
    "ASUSTeK COMPUTER INC.",
    "ASUSTek Computer Inc.",
    "Plex, Inc.",
    "DTS, Inc.",
    "Logitech Inc",
    "Logitech Inc.",
    "Gaijin Network Ltd",
    "Nefarius Software Solutions e.U.",
    "Riot Games, Inc",
    "Roblox Corporation",
    "Rockstar Games",
    "ROBLOX Corporation",
    "win.rar GmbH",
    "Microsoft Studios",
    "WHIRLWIND VIRTUAL REALITIES INC.",
    "Noriyuki MIYAZAKI",
    "Blizzard Entertainment",
    "BeamMP",
    "VoodooSoft, LLC",
    "(NVIDIA Corp.)",
    "Reincubate Ltd",
    "(Team Cherry)",
    "LunarG, Inc.",
    "Python Software Foundation",
    "Parsec Cloud Inc.",
    "Microsoft Corporation",
    "Oracle Corporation",
    "Epic Games, Inc.",
    "AutoHotkey Foundation LLC",
    "Igor Pavlov",
    "FOXIT SOFTWARE INC.",
    "philandro Software GmbH",
    "AnyDesk Software GmbH",
    "Foxit Software Inc.",
    "The Git Development Community",
    "Skutta, Kristjan",
    "Proton Technologies AG",
    "Jagex Limited",
    "Activision Publishing Inc",
    "Activision Blizzard, Inc.",
    "Micro-Star Int'l Co. Ltd.",
    "VS Revo Group Ltd.",
    "VS Revo Group",
    "Jagex Ltd",
    "Mozilla",
    "Nicholas H.Tollervey",
    "Newgrounds",
    "OBS Project",
    "Proton AG",
    "TeamViewer",
    "RuneLite",
    "Realtek",
    "PROXIMA BETA PTE. LIMITED",
    "KRAFTON, Inc.",
    "Advanced Micro Devices INC.",
    "Advanced Micro Devices",
    "LG Electronics Inc.",
    "Snap Inc.",
    "GOG  sp. z o.o",
    "GOG.com",
    "FACE IT LIMITED",
    "tinyBuild Games",
    "Wellbia.com Co., Ltd.",
    "Audacity Team",
    "CPUID, Inc.",
    "Bethesda Softworks",
    "BANDAI NAMCO Entertainment Inc.",
    "WhatsApp Inc.",
    "TechPowerUp LLC",
    "Ubisoft Entertainment Sweden AB",
    "Ring.com",
    "NZXT, Inc.",
    "Wondershare Technology Group Co.,Ltd",
    "Wondershare",
    "Voyetra Turtle Beach, Inc.",
    "ROCCAT",
    "Ferox Games B.V.",
    "Spotify Ltd",
    "Medal B.V.",
    "Logitech",
    "Lexikos",
    "Voicemod Sociedad Limitada",
    "Voicemod",
    "GoPro Inc.",
    "Twitch Interactive, Inc.",
    "Facebook, Inc.",
    "Chris Andriessen",
    "Moonsworth, LLC",
    "Now.gg, INC",
    "Vincent Burel",
    "Windows (R) Win 7 DDK provider",
    "(AMD)",
    "Disney",
    "Charles Milette",
    "Bandicam Company",
    "Conexant Systems LLC.",
    "The Qt Company Ltd.",
    "F.lux Software LLC",
    "f.lux Software LLC",
    ": %windir%\system32\compattelrunner.exe",
    "Synaptics Hong Kong Limited, Taiwan Branch (H.K.)",
    "TRACKER SOFTWARE PRODUCTS (CANADA) LIMITED",
    "Tracker Software Products (Canada) Ltd.",
    "Electronic Arts",
    "TranslucentTB Open Source Developers",
    "MSI Co., LTD",
    "Axiw Software",
    "Signify Netherlands B.V.",
    "rocksdanister",
    "Oculus VR, LLC",
    "Facebook Technologies, LLC",
    "Zoom Video Communications, Inc.",
    "Unity Technologies ApS",
    "Unity Technologies Inc.",
    "Ubisoft",
    "Chrome\\User Data\System Profile [",
    "ManyCam (VISICOM MÉDIA INC.)",
    "Visicom Media Inc.",
    "WindowsLiveWallpaper",
    "Chan Software Solutions",
    "Instagram",
    "Amazon Development Centre (London) Ltd",
    "Rémi Mercier",
    "Whirlwind FX (Whirlwind Virtual Realities Inc.)",
    "(Microsoft)",
    "ppy Pty Ltd",
    "Crystal Dew World",
    "(Meta)",
    "TranslucentTB",
    "CyberLink Corp.",
    "CyberLink",
    "GoPro Media, Inc.",
    "Hewlett-Packard Development Company, L.P.",
    "Virtual Desktop, Inc.",
    "BUREL VINCENT",
    "VB-AUDIO Software",
    "Silicon Motion, Inc.",
    "(Facebook Inc.)",
    "VB-Audio Software",
    "Red Giant   LLC",
    "Red Giant LLC",
    "Focusrite Audio Engineering Ltd.",
    "Focusrite Audio Engineering Ltd",
    "Focusrite Audio Engineering, Ltd.",
    "Psyonix, LLC",
    "(BetterDiscord)",
    "Bytedance Pte. Ltd.",
    "Mojang AB",
    "Mojang",
    "DISPLAYLINK (UK) LIMITED",
    "DisplayLink Corp.",
    "ASUSTek COMPUTER INC.",
    "(AMD Inc.)",
    "Docker Inc",
    "(ELAN Microelectronic Corp.)",
    "LIAN LI INDUSTRIAL CO., LTD.",
    "Lian-Li",
    "MUSIC Tribe Brands DE GmbH",
    "TC-Helicon Vocal Technologies Inc.",
    "Alexey Nicolaychuk",
    "Florian Höch",
    "Duet, Inc.",
    "Hugh Bailey",
    "Shenzhen Huion Animation Technology Co.,LTD",
    "ICEpower a/s",
    "ICEpower A/S",
    "COGNOSPHERE PTE. LTD.",
    "HoYoverse",
    "Corsair Components, Inc.",
    "Dell Technologies",
    "Monect (Suzhou) Co., Ltd.",
    "Monect, Inc.",
    "KRAFTON, Inc",
    "Stardock Corporation",
    "Stardock Software, Inc",
    "STARDOCK SYSTEMS, INC.",
    "Micro-Star INT'L CO., LTD.",
    "Sony Corporation",
    "ASUS",
    "ASUSTeK Computer Inc.",
    "ASUSTeK COMPUTER INC.",
    "KINGSTON COMPONENTS INC.",
    "Adobe Inc.",
    "Adobe Systems",
    "Voicemod Sociedad Limitada",
    "Voicemod",
    "win.rar GmbH",
    "Alexander Roshal",
}

IMPORTANT_STRINGS = {
    "<==== ATTENTION",
    "No File",
    "File not signed",
    "[not found]",
    "[X]",
    "Hidden",
    "no ImagePath",
    "detected!",
    "powershell",
}

WHITE_LIST = set()


# ============================================================
# FRST Cleaning Logic
# ============================================================
def should_remove_line(line):
    contains_clean_string = any(clean_string in line for clean_string in CLEAN_STRINGS)
    contains_important_string = any(important_string in line for important_string in IMPORTANT_STRINGS)
    contains_white_list_string = any(white_string in line for white_string in WHITE_LIST)
    return contains_clean_string and not contains_important_string and not contains_white_list_string


def clean_log_content(lines):
    cleaned_lines = []
    removed_lines = []

    for line in lines:
        processed_line = line.replace("\u00AE", "(R)").replace("Ã‚", "")
        if should_remove_line(processed_line):
            removed_lines.append(line)
        else:
            cleaned_lines.append(line)

    return cleaned_lines, removed_lines


# ============================================================
# Color Definitions for Syntax Highlighting
# ============================================================
FLAG_COLORS = {
    "<==== ATTENTION": "#ff5555",
    "No File": "#00ff66",
    "File not signed": "#ff7700",
    "[not found]": "#ffff00",
    "[X]": "#ffff00",
    "Hidden": "#4488ff",
    "no ImagePath": "#ffff00",
    "detected!": "#ff5555",
    "powershell": "#ff5555",
}

FLAG_PRIORITY = {
    "<==== ATTENTION": 10,
    "detected!": 9,
    "powershell": 9,
    "File not signed": 8,
    "[not found]": 7,
    "[X]": 7,
    "no ImagePath": 7,
    "Hidden": 6,
    "No File": 5,
}


def get_line_flags(line):
    flags = []
    for keyword in FLAG_COLORS:
        if keyword in line:
            flags.append(keyword)
    return flags


def get_line_color(line):
    flags = get_line_flags(line)
    if not flags:
        return None

    # Use keyword-based priority
    best_color = None
    best_priority = -1
    for flag in flags:
        priority = FLAG_PRIORITY.get(flag, 0)
        if priority > best_priority:
            best_priority = priority
            best_color = FLAG_COLORS[flag]

    return best_color


# ============================================================
# Custom Text Widget with Syntax Highlighting
# ============================================================
class FRSTText(tk.Text):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.bind('<KeyRelease>', self.on_key_release)
        self.original_content = ""
        self.is_cleaned = False
        self.cleaned_lines = []
        self.removed_lines = []
        self.file_path = None
        self.file_name = "Untitled"
        self.is_frst_log = False
        self.modified = False
        self.parent_notepad = None
        self.current_theme = "dark"

        self.tag_configure("red", foreground="#ff5555")
        self.tag_configure("green", foreground="#00ff66")
        self.tag_configure("orange", foreground="#ff7700")
        self.tag_configure("yellow", foreground="#ffff00")
        self.tag_configure("blue", foreground="#4488ff")
        self.tag_configure("search_highlight", background="#333355")

    def on_key_release(self, event):
        self.modified = True
        self.highlight_syntax()
        if self.parent_notepad:
            self.parent_notepad.update_status()
            self.parent_notepad.update_tab_title()

    def set_theme(self, theme):
        self.current_theme = theme
        if theme == "dark":
            self.configure(bg="#1e1e1e", fg="#d4d4d4", insertbackground="#d4d4d4")
            self.tag_configure("search_highlight", background="#333355")
        else:
            self.configure(bg="#ffffff", fg="#000000", insertbackground="#000000")
            self.tag_configure("search_highlight", background="#ffff99")

    def set_content(self, content, file_path=None, file_name="Untitled", is_frst=False):
        self.file_path = file_path
        self.file_name = file_name
        self.is_frst_log = is_frst
        self.original_content = content

        self.delete('1.0', tk.END)
        self.insert('1.0', content)
        self.highlight_syntax()
        self.modified = False

    def get_content(self):
        content = self.get('1.0', tk.END)
        if content.endswith('\n') and content != '\n':
            content = content.rstrip('\n')
        return content

    def get_line_count(self):
        """Get the number of lines in the document."""
        content = self.get_content()
        if not content:
            return 0
        return content.count('\n') + 1

    def highlight_syntax(self):
        for tag in ["red", "green", "orange", "yellow", "blue"]:
            self.tag_remove(tag, '1.0', tk.END)

        content = self.get_content()
        lines = content.split('\n')

        for i, line in enumerate(lines):
            if not line:
                continue

            line_start = f"{i+1}.0"
            line_end = f"{i+1}.end"

            color = get_line_color(line)
            if color:
                tag_name = {
                    "#ff5555": "red",
                    "#00ff66": "green",
                    "#ff7700": "orange",
                    "#ffff00": "yellow",
                    "#4488ff": "blue"
                }.get(color)

                if tag_name:
                    self.tag_add(tag_name, line_start, line_end)

    def clean_log(self):
        if not self.is_frst_log:
            return None, None

        # Use current content, not original
        lines = self.get_content().split('\n')
        cleaned_lines, removed_lines = clean_log_content(lines)

        self.cleaned_lines = cleaned_lines
        self.removed_lines = removed_lines
        self.is_cleaned = True

        cleaned_content = '\n'.join(cleaned_lines)
        self.delete('1.0', tk.END)
        self.insert('1.0', cleaned_content)
        self.highlight_syntax()
        self.modified = True

        return cleaned_lines, removed_lines

    def revert_to_original(self):
        if not self.is_frst_log:
            return

        self.delete('1.0', tk.END)
        self.insert('1.0', self.original_content)
        self.highlight_syntax()
        self.is_cleaned = False
        self.modified = True


# ============================================================
# Custom Tab with Close Button
# ============================================================
class ClosableTab:
    def __init__(self, notebook, text, parent):
        self.notebook = notebook
        self.parent = parent
        self.frame = ttk.Frame(notebook)
        self.tab_id = None

        # Create text widget with Sublime-like font
        self.text_widget = FRSTText(
            self.frame,
            wrap=tk.NONE,
            font=("Consolas", 11),
            bg="#1e1e1e",
            fg="#d4d4d4",
            insertbackground="#d4d4d4",
            relief=tk.FLAT,
            borderwidth=0
        )
        self.text_widget.parent_notepad = parent

        # Create scrollbars
        vsb = ttk.Scrollbar(self.frame, orient="vertical", command=self.text_widget.yview)
        hsb = ttk.Scrollbar(self.frame, orient="horizontal", command=self.text_widget.xview)
        self.text_widget.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        # Layout: text widget with scrollbars
        self.text_widget.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")

        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        # Add tab to notebook
        self.notebook.add(self.frame, text=text)

    def close(self):
        """Close this tab."""
        if self.text_widget.modified:
            result = messagebox.askyesnocancel("Unsaved Changes",
                f"'{self.text_widget.file_name}' has been modified. Save before closing?")
            if result is None:
                return False
            if result:
                self.parent.save_file()

        self.notebook.forget(self.frame)
        self.frame.destroy()
        return True

    def get_text_widget(self):
        return self.text_widget


# ============================================================
# Main Application
# ============================================================
class FRSTNotepad:
    def __init__(self, root):
        self.root = root
        self.root.title("FRST Log Notepad")
        self.root.geometry("1100x750")
        self.root.minsize(800, 500)

        self.tabs = []
        self.tab_counter = 0
        self.current_tab = None
        self.current_theme = "dark"

        self.create_menu()
        self.create_toolbar()
        self.create_notebook()
        self.create_status_bar()
        self.bind_shortcuts()

        # Bind window close event
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        # Start with no tabs - will create tab when user types or opens a file

    def create_menu(self):
        menubar = tk.Menu(self.root)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_command(label="Save As", command=self.save_as, accelerator="Ctrl+Shift+S")
        file_menu.add_separator()
        file_menu.add_command(label="Close Tab", command=self.close_tab, accelerator="Ctrl+W")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.on_close, accelerator="Ctrl+Q")
        menubar.add_cascade(label="File", menu=file_menu)

        tools_menu = tk.Menu(menubar, tearoff=0)
        tools_menu.add_command(label="Clean All Logs", command=self.clean_all_logs, accelerator="Ctrl+Shift+C")
        tools_menu.add_command(label="Revert to Original", command=self.revert_current_log, accelerator="Ctrl+Shift+R")
        tools_menu.add_command(label="View Whitelist", command=self.open_whitelist, accelerator="Ctrl+Shift+W")
        menubar.add_cascade(label="Tools", menu=tools_menu)

        view_menu = tk.Menu(menubar, tearoff=0)
        view_menu.add_command(label="Dark Theme", command=lambda: self.set_theme("dark"))
        view_menu.add_command(label="Light Theme", command=lambda: self.set_theme("light"))
        menubar.add_cascade(label="View", menu=view_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Keyboard Shortcuts", command=self.show_shortcuts)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menubar)

    def create_toolbar(self):
        """Create toolbar with + button and close button."""
        self.toolbar = ttk.Frame(self.root)
        self.toolbar.pack(fill=tk.X, padx=5, pady=(5, 0))

        # + button for new tab
        self.new_tab_btn = ttk.Button(
            self.toolbar,
            text="➕",
            width=3,
            command=self.new_blank_tab
        )
        self.new_tab_btn.pack(side=tk.LEFT, padx=(0, 5))

        # Separator
        ttk.Separator(self.toolbar, orient="vertical").pack(side=tk.LEFT, fill=tk.Y, padx=2)

        # Close tab button
        self.close_tab_btn = ttk.Button(
            self.toolbar,
            text="✕",
            width=3,
            command=self.close_tab
        )
        self.close_tab_btn.pack(side=tk.LEFT, padx=2)

        # Spacer
        ttk.Label(self.toolbar, text="").pack(side=tk.LEFT, expand=True, fill=tk.X)

        # Tab name display
        self.tab_name_label = ttk.Label(self.toolbar, text="", font=("Segoe UI", 9))
        self.tab_name_label.pack(side=tk.RIGHT, padx=5)

    def create_notebook(self):
        """Create the notebook as the main area."""
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.notebook.bind("<<NotebookTabChanged>>", self.on_tab_changed)

        # Bind key events to create tab when typing
        self.root.bind('<Key>', self.on_key_press)

    def create_status_bar(self):
        self.status_frame = ttk.Frame(self.root)
        self.status_frame.pack(fill=tk.X, padx=5, pady=2)

        self.line_label = ttk.Label(self.status_frame, text="Line: 0")
        self.line_label.pack(side=tk.LEFT, padx=5)

        self.flags_label = ttk.Label(self.status_frame, text="Flags: 0")
        self.flags_label.pack(side=tk.LEFT, padx=10)

        self.removed_label = ttk.Label(self.status_frame, text="Removed: 0")
        self.removed_label.pack(side=tk.LEFT, padx=10)

        self.search_var = tk.StringVar()
        self.search_var.trace_add('write', self.on_search)

        search_label = ttk.Label(self.status_frame, text="🔍 Search:")
        search_label.pack(side=tk.RIGHT, padx=2)

        self.search_entry = ttk.Entry(self.status_frame, textvariable=self.search_var, width=30)
        self.search_entry.pack(side=tk.RIGHT, padx=5)

    def bind_shortcuts(self):
        self.root.bind('<Control-o>', lambda e: self.open_file())
        self.root.bind('<Control-s>', lambda e: self.save_file())
        self.root.bind('<Control-S>', lambda e: self.save_as())
        self.root.bind('<Control-w>', lambda e: self.close_tab())
        self.root.bind('<Control-q>', lambda e: self.on_close())
        self.root.bind('<Control-Shift-C>', lambda e: self.clean_all_logs())
        self.root.bind('<Control-Shift-R>', lambda e: self.revert_current_log())
        self.root.bind('<Control-Shift-W>', lambda e: self.open_whitelist())
        self.root.bind('<Control-t>', lambda e: self.new_blank_tab())
        # Tab navigation
        self.root.bind('<Control-Tab>', lambda e: self.next_tab())
        self.root.bind('<Control-Shift-Tab>', lambda e: self.prev_tab())

    def next_tab(self):
        """Switch to the next tab."""
        if len(self.tabs) <= 1:
            return
        current = self.get_current_tab()
        if current:
            idx = self.tabs.index(current)
            next_idx = (idx + 1) % len(self.tabs)
            self.notebook.select(self.tabs[next_idx].frame)
            self.update_status()

    def prev_tab(self):
        """Switch to the previous tab."""
        if len(self.tabs) <= 1:
            return
        current = self.get_current_tab()
        if current:
            idx = self.tabs.index(current)
            prev_idx = (idx - 1) % len(self.tabs)
            self.notebook.select(self.tabs[prev_idx].frame)
            self.update_status()

    def on_close(self):
        """Handle window close event - check for unsaved changes."""
        unsaved = []
        for tab in self.tabs:
            if tab.text_widget.modified:
                unsaved.append(tab.text_widget.file_name)

        if unsaved:
            result = messagebox.askyesnocancel("Unsaved Changes",
                f"The following tabs have unsaved changes:\n\n{chr(10).join(unsaved)}\n\nSave before closing?")
            if result is None:
                return  # Cancel close
            if result:
                # Save all unsaved tabs
                for tab in self.tabs:
                    if tab.text_widget.modified:
                        self.save_file()
                # If any save failed or user canceled, we stay open
                # But for simplicity, let's just check if there are still modified tabs
                still_unsaved = any(tab.text_widget.modified for tab in self.tabs)
                if still_unsaved:
                    return

        self.root.quit()

    def on_key_press(self, event):
        """Create a tab when user starts typing."""
        # Ignore modifier keys, function keys, and navigation keys
        if len(event.char) == 0 or event.char in ['\x01', '\x16', '\x18', '\x19', '\x1b']:
            return
        if event.keysym in ['Control_L', 'Control_R', 'Shift_L', 'Shift_R', 'Alt_L', 'Alt_R']:
            return

        # Check if there are any tabs
        if len(self.tabs) == 0:
            # Create a new tab and insert the character
            tab = self.new_blank_tab()
            tab.text_widget.insert('1.0', event.char)
            tab.text_widget.modified = True
            self.update_status()

    def set_theme(self, theme):
        """Set the theme for all text widgets."""
        self.current_theme = theme
        for tab in self.tabs:
            tab.text_widget.set_theme(theme)

    def new_blank_tab(self):
        """Create a new blank tab."""
        return self.new_tab(file_name="Untitled")

    def new_tab(self, content="", file_path=None, file_name="Untitled", is_frst=False):
        """Create a new tab."""
        self.tab_counter += 1

        # Create a closable tab
        tab = ClosableTab(self.notebook, file_name, self)
        tab.text_widget.set_content(content, file_path, file_name, is_frst)
        tab.text_widget.set_theme(self.current_theme)

        self.tabs.append(tab)

        # Update tab name display
        self.tab_name_label.config(text=file_name)

        # Select the new tab
        self.notebook.select(tab.frame)

        self.update_status()

        return tab

    def get_current_tab(self):
        """Get the currently selected tab."""
        if len(self.tabs) == 0:
            return None
        current = self.notebook.select()
        if not current:
            return None
        for tab in self.tabs:
            if str(tab.frame) == str(current):
                return tab
        return None

    def get_current_text_widget(self):
        """Get the currently selected text widget."""
        tab = self.get_current_tab()
        if tab:
            return tab.text_widget
        return None

    def on_tab_changed(self, event):
        self.update_status()
        tab = self.get_current_tab()
        if tab:
            self.tab_name_label.config(text=tab.text_widget.file_name)

    def update_status(self):
        """Update status bar information."""
        widget = self.get_current_text_widget()
        if not widget:
            self.line_label.config(text="Line: 0")
            self.flags_label.config(text="Flags: 0")
            self.removed_label.config(text="Removed: 0")
            return

        content = widget.get_content()
        lines = content.split('\n') if content else []
        line_count = len(lines)

        flag_count = 0
        for line in lines:
            if get_line_flags(line):
                flag_count += 1

        self.line_label.config(text=f"Line: {line_count}")
        self.flags_label.config(text=f"Flags: {flag_count}")

        if widget.is_cleaned and widget.removed_lines:
            self.removed_label.config(text=f"Removed: {len(widget.removed_lines)}")
        else:
            self.removed_label.config(text="Removed: 0")

        self.update_tab_title()

    def on_search(self, *args):
        query = self.search_var.get().strip()
        widget = self.get_current_text_widget()
        if not widget:
            return

        widget.tag_remove("search_highlight", '1.0', tk.END)

        if not query:
            return

        start = '1.0'
        first_match = None
        while True:
            pos = widget.search(query, start, tk.END, nocase=True)
            if not pos:
                break
            if first_match is None:
                first_match = pos
            end = f"{pos}+{len(query)}c"
            widget.tag_add("search_highlight", pos, end)
            start = end

        # Jump to first match
        if first_match:
            widget.see(first_match)

    def open_file(self):
        """Open files. Supports multiple file selection."""
        file_paths = filedialog.askopenfilenames(
            title="Open Files",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if not file_paths:
            return

        # Check for duplicate filenames
        existing_names = [tab.text_widget.file_name for tab in self.tabs]
        for file_path in file_paths:
            file_name = os.path.basename(file_path)
            if file_name in existing_names:
                result = messagebox.askyesno("File Already Open",
                    f"'{file_name}' is already open. Open it again?")
                if not result:
                    continue

            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                is_frst = file_name.lower() in ["frst.txt", "addition.txt"]

                self.new_tab(content, file_path, file_name, is_frst)

            except Exception as e:
                messagebox.showerror("Error", f"Could not open file: {e}")

    def save_file(self):
        widget = self.get_current_text_widget()
        if not widget:
            return

        if widget.file_path:
            try:
                content = widget.get_content()
                with open(widget.file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                widget.modified = False
                widget.original_content = content  # Update original_content after save
                self.update_tab_title()
                messagebox.showinfo("Success", f"File saved: {widget.file_name}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {e}")
        else:
            self.save_as()

    def save_as(self):
        widget = self.get_current_text_widget()
        if not widget:
            return

        file_path = filedialog.asksaveasfilename(
            title="Save As",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if not file_path:
            return

        try:
            content = widget.get_content()
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            widget.file_path = file_path
            widget.file_name = os.path.basename(file_path)
            widget.modified = False
            widget.original_content = content  # Update original_content after save

            self.update_tab_title()
            self.tab_name_label.config(text=widget.file_name)
            messagebox.showinfo("Success", f"File saved: {widget.file_name}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file: {e}")

    def update_tab_title(self):
        """Update the tab title for the current widget."""
        tab = self.get_current_tab()
        if not tab:
            return

        title = tab.text_widget.file_name
        if tab.text_widget.modified:
            title += " *"
        self.notebook.tab(tab.frame, text=title)

    def close_tab(self):
        """Close the current tab."""
        tab = self.get_current_tab()
        if not tab:
            return

        # Allow zero tabs - just remove the tab
        # If it was modified, ask to save
        if tab.text_widget.modified:
            result = messagebox.askyesnocancel("Unsaved Changes",
                f"'{tab.text_widget.file_name}' has been modified. Save before closing?")
            if result is None:
                return
            if result:
                self.save_file()
                # If still modified after save attempt, don't close
                if tab.text_widget.modified:
                    return

        # Close the tab
        if tab.close():
            self.tabs.remove(tab)
            self.update_status()
            if len(self.tabs) == 0:
                self.tab_name_label.config(text="No tabs")
            else:
                current_tab = self.get_current_tab()
                if current_tab:
                    self.tab_name_label.config(text=current_tab.text_widget.file_name)

    def clean_all_logs(self):
        """Clean ALL FRST logs in all tabs, not just the current one."""
        cleaned_any = False
        all_removed = {}
        cleaned_count = 0
        total_removed_count = 0

        for tab in self.tabs:
            widget = tab.text_widget
            if widget.is_frst_log:
                # Skip if already cleaned
                if widget.is_cleaned:
                    cleaned_count += 1
                    continue

                cleaned_lines, removed_lines = widget.clean_log()
                if cleaned_lines is not None:
                    cleaned_any = True
                    file_name = widget.file_name.replace('.txt', '')
                    if removed_lines and len(removed_lines) > 0:
                        all_removed[file_name] = removed_lines
                        total_removed_count += len(removed_lines)

        if not cleaned_any:
            # Check if any were already cleaned
            already_cleaned = any(tab.text_widget.is_frst_log and tab.text_widget.is_cleaned for tab in self.tabs)
            if already_cleaned:
                result = messagebox.askyesno("Already Cleaned",
                    "Some logs are already cleaned. Re-clean all FRST logs?")
                if result:
                    # Force re-clean all
                    all_removed = {}
                    total_removed_count = 0
                    for tab in self.tabs:
                        widget = tab.text_widget
                        if widget.is_frst_log:
                            # Reset cleaned state and re-clean
                            widget.is_cleaned = False
                            cleaned_lines, removed_lines = widget.clean_log()
                            if removed_lines and len(removed_lines) > 0:
                                file_name = widget.file_name.replace('.txt', '')
                                all_removed[file_name] = removed_lines
                                total_removed_count += len(removed_lines)
                    if all_removed:
                        self.open_whitelist()
                    self.update_status()
                return
            else:
                messagebox.showinfo("Info", "No FRST logs found to clean.")
                return

        self.update_status()

        if all_removed:
            self.open_whitelist()
            messagebox.showinfo("Cleaned", f"All logs cleaned. {total_removed_count} total entries removed.")
        else:
            messagebox.showinfo("Cleaned", "Logs cleaned. No entries were removed.")

    def revert_current_log(self):
        widget = self.get_current_text_widget()
        if not widget:
            return

        if not widget.is_frst_log:
            return

        widget.revert_to_original()
        self.update_status()

    def open_whitelist(self):
        """Open the whitelisted strings from ALL cleaned logs in a single tab."""
        all_removed = {}
        for tab in self.tabs:
            widget = tab.text_widget
            if widget.is_frst_log and widget.is_cleaned and widget.removed_lines:
                file_name = widget.file_name.replace('.txt', '')
                all_removed[file_name] = widget.removed_lines

        if not all_removed:
            messagebox.showinfo("Info", "No entries were removed. Whitelist is empty.")
            return

        whitelist_content = ""
        for file_name, removed_lines in all_removed.items():
            whitelist_content += f"============================={file_name} Removed Entries=============================\n"
            whitelist_content += '\n'.join(removed_lines)
            whitelist_content += "\n\n"

        # Check if whitelist tab already exists and update it, or create new one
        for tab in self.tabs:
            if tab.text_widget.file_name == "Whitelisted_Strings.txt":
                tab.text_widget.delete('1.0', tk.END)
                tab.text_widget.insert('1.0', whitelist_content)
                tab.text_widget.highlight_syntax()
                self.notebook.select(tab.frame)
                return

        self.new_tab(whitelist_content, file_path=None, file_name="Whitelisted_Strings.txt", is_frst=False)

    def show_shortcuts(self):
        shortcuts = """Keyboard Shortcuts:

        Ctrl+O          Open file(s)
        Ctrl+S          Save current tab
        Ctrl+Shift+S    Save As
        Ctrl+W          Close tab
        Ctrl+Q          Exit
        Ctrl+T          New tab
        Ctrl+Shift+C    Clean ALL logs
        Ctrl+Shift+R    Revert to original
        Ctrl+Shift+W    View Whitelist
        Ctrl+Tab        Next tab
        Ctrl+Shift+Tab  Previous tab

        Search is always available in the status bar."""
        messagebox.showinfo("Keyboard Shortcuts", shortcuts)

    def show_about(self):
        about = """FRST Log Notepad v1.0

        A dedicated notepad for FRST log analysis.

        Features:
        - Multi-tab support with close buttons
        - Clean ALL FRST logs at once
        - Color-coded flagging
        - Combined whitelist generation
        - Dark/Light theme toggle
        - Multiple file selection
        - Sublime-like font (Consolas)

        Built for malware removal triage.

        Forked and improved from the original FRST log cleaner.
        Original by SkeletalDemise."""
        messagebox.showinfo("About", about)


def main():
    root = tk.Tk()
    app = FRSTNotepad(root)
    root.mainloop()


if __name__ == "__main__":
    main()