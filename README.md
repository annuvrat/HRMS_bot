# HRMS Clock In/Out Automation 🕒

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Selenium](https://img.shields.io/badge/selenium-4.0+-green.svg)](https://www.selenium.dev/)

Automate your daily HRMS clock-in and clock-out process with this Python script. Built with Selenium, it handles the routine task of logging your work hours while you focus on what matters.

## 🌟 Features

- **Automated Login**: Securely log into your HRMS portal
- **Smart Scheduling**: Runs only on workdays (Monday to Friday)
- **Flexible Configuration**: Easy to customize work hours and credentials
- **Error Handling**: Robust error management with detailed logging
- **Headless Mode**: Run in background without browser UI
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 📋 Prerequisites

Before you begin, ensure you have:

- Python 3.8 or higher
- Google Chrome browser
- Chrome WebDriver (matching your Chrome version)
- pip (Python package manager)

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/hrms-automation.git
   cd hrms-automation
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your credentials (optional)**
   ```bash
   # Create a config.json file with your details
   {
     "hrms_url": "https://hrms.yourdomain.com",
     "email": "your.email@company.com",
     "password": "your-password",
     "work_hours": 9,
     "headless": true
   }
   ```

4. **Run the script**
   ```bash
   python hrms_automation.py
   ```

## ⚙️ Configuration Options

| Option | Description | Default |
|--------|-------------|---------|
| `hrms_url` | Your HRMS portal URL | `https://hrms.example.com` |
| `email` | Your login email | None |
| `password` | Your login password | None |
| `work_hours` | Hours between clock-in and clock-out | 9 |
| `headless` | Run browser in headless mode | `true` |
| `check_weekends` | Skip execution on weekends | `true` |

## 🔄 Automation Setup

### Windows Task Scheduler

1. Open Task Scheduler
2. Click "Create Basic Task"
3. Set trigger to "Daily" at your work start time
4. Action: Start Program
5. Program/script: `python`
6. Arguments: `path\to\hrms_automation.py`

### macOS (Crontab)

1. Open Terminal
2. Edit crontab: `crontab -e`
3. Add line for weekday execution at 9 AM:
   ```bash
   0 9 * * 1-5 /usr/bin/python3 /path/to/hrms_automation.py
   ```

### Linux (Systemd)

1. Create a service file:
   ```bash
   sudo nano /etc/systemd/system/hrms-automation.service
   ```

2. Add configuration:
   ```ini
   [Unit]
   Description=HRMS Automation Service
   
   [Service]
   ExecStart=/usr/bin/python3 /path/to/hrms_automation.py
   User=yourusername
   
   [Install]
   WantedBy=multi-user.target
   ```

3. Enable and start:
   ```bash
   sudo systemctl enable hrms-automation
   sudo systemctl start hrms-automation
   ```

## 📝 Logging

Logs are stored in `hrms_automation.log` with the following information:
- Login attempts
- Clock in/out status
- Errors and exceptions
- Script execution details

## 🛠️ Troubleshooting

Common issues and solutions:

1. **ChromeDriver version mismatch**
   ```bash
   # Check Chrome version
   google-chrome --version
   # Download matching ChromeDriver from:
   # https://chromedriver.chromium.org/downloads
   ```

2. **Element not found errors**
   - Verify HRMS portal structure hasn't changed
   - Check network connectivity
   - Increase wait time in config

3. **Authentication failures**
   - Verify credentials in config.json
   - Check if password reset is required
   - Ensure no CAPTCHA is present

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ⚠️ Disclaimer

This script is for educational purposes only. Ensure you have permission to automate your HRMS system before use. The author is not responsible for any misuse or consequences.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Selenium WebDriver team
- Chrome WebDriver developers


---
Made with ❤️ by Annuvrat
