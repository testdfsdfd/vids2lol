import os
from flask import Flask
import json

app = Flask(__name__)

def generate_video_gallery():
    # Folder containing videos
    videos_dir = os.path.join(os.path.dirname(__file__), "static", "videos")

    # Make sure the folder exists
    if not os.path.exists(videos_dir):
        os.makedirs(videos_dir, exist_ok=True)
        return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Video Gallery</title>
            <style>
                body { 
                    font-family: 'Segoe UI', system-ui, sans-serif; 
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    color: white;
                    text-align: center;
                }
                .error-container {
                    background: rgba(255,255,255,0.1);
                    backdrop-filter: blur(10px);
                    padding: 3rem;
                    border-radius: 20px;
                    border: 1px solid rgba(255,255,255,0.2);
                }
            </style>
        </head>
        <body>
            <div class="error-container">
                <h2>Welcome to Video Gallery!</h2>
                <p>No videos found yet. Upload videos to the 'static/videos' folder.</p>
            </div>
        </body>
        </html>
        """

    # Supported video formats
    video_extensions = (".mp4", ".webm", ".ogg", ".mov", ".mkv", ".avi")

    # List all video files
    videos = [f for f in os.listdir(videos_dir) if f.lower().endswith(video_extensions)]

    if not videos:
        return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Video Gallery</title>
            <style>
                body { 
                    font-family: 'Segoe UI', system-ui, sans-serif; 
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    color: white;
                    text-align: center;
                }
                .error-container {
                    background: rgba(255,255,255,0.1);
                    backdrop-filter: blur(10px);
                    padding: 3rem;
                    border-radius: 20px;
                    border: 1px solid rgba(255,255,255,0.2);
                }
            </style>
        </head>
        <body>
            <div class="error-container">
                <h2>Ready for videos!</h2>
                <p>Add video files to the 'static/videos' folder and refresh the page.</p>
            </div>
        </body>
        </html>
        """

    # Build HTML with modern design
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Video Gallery</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', system-ui, sans-serif;
            background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
            color: #ffffff;
            min-height: 100vh;
            line-height: 1.6;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }}

        .header {{
            text-align: center;
            margin-bottom: 3rem;
            position: relative;
        }}

        .header h1 {{
            font-size: 3.5rem;
            background: linear-gradient(45deg, #00ffff, #ff00ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 0.5rem;
            font-weight: 800;
        }}

        .header p {{
            color: #8892b0;
            font-size: 1.2rem;
        }}

        .stats {{
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-top: 1rem;
            flex-wrap: wrap;
        }}

        .stat-item {{
            background: rgba(255,255,255,0.1);
            padding: 0.5rem 1rem;
            border-radius: 10px;
            border: 1px solid rgba(255,255,255,0.2);
        }}

        .video-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }}

        .video-card {{
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 1.5rem;
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }}

        .video-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
            transition: left 0.5s ease;
        }}

        .video-card:hover::before {{
            left: 100%;
        }}

        .video-card:hover {{
            transform: translateY(-10px);
            border-color: rgba(0, 255, 255, 0.3);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        }}

        .video-card h3 {{
            color: #00ffff;
            margin-bottom: 1rem;
            font-size: 1.3rem;
            text-align: center;
            padding: 0.5rem;
            border-bottom: 1px solid rgba(0, 255, 255, 0.2);
        }}

        .video-player {{
            width: 100%;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        }}

        video {{
            width: 100%;
            height: auto;
            display: block;
            background: #000;
        }}

        .video-info {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 1rem;
            padding: 0 0.5rem;
            color: #8892b0;
            font-size: 0.9rem;
        }}

        .file-size {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .file-type {{
            background: rgba(0, 255, 255, 0.1);
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            border: 1px solid rgba(0, 255, 255, 0.3);
        }}

        .footer {{
            text-align: center;
            margin-top: 4rem;
            color: #8892b0;
            padding: 2rem 0;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }}

        .auto-refresh {{
            background: rgba(0, 255, 255, 0.1);
            padding: 1rem;
            border-radius: 10px;
            margin: 1rem 0;
            border: 1px solid rgba(0, 255, 255, 0.3);
        }}

        @media (max-width: 768px) {{
            .video-grid {{
                grid-template-columns: 1fr;
            }}
            
            .header h1 {{
                font-size: 2.5rem;
            }}
            
            .container {{
                padding: 1rem;
            }}
        }}

        /* Loading animation */
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(30px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .video-card {{
            animation: fadeIn 0.6s ease forwards;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1><i class="fas fa-play-circle"></i> Video Gallery</h1>
            <p>Auto-generated video collection</p>
            <div class="stats">
                <div class="stat-item">
                    <i class="fas fa-video"></i> {len(videos)} videos
                </div>
                <div class="stat-item">
                    <i class="fas fa-sync-alt"></i> Auto-refresh on changes
                </div>
            </div>
        </div>

        <div class="auto-refresh">
            <i class="fas fa-info-circle"></i> 
            Add videos to the <code>static/videos</code> folder and refresh the page
        </div>

        <div class="video-grid">
"""

    total_size = 0
    for video in videos:
        video_path = os.path.join(videos_dir, video)
        file_size = 0
        
        try:
            # Get file size in MB
            size_bytes = os.path.getsize(video_path)
            file_size = size_bytes
            total_size += size_bytes
            file_size_display = f"{size_bytes / (1024 * 1024):.1f} MB"
        except:
            file_size_display = "Unknown"
        
        file_ext = os.path.splitext(video)[1][1:].upper()
        
        html += f"""
            <div class="video-card">
                <h3>{video}</h3>
                <div class="video-player">
                    <video controls poster="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='225' viewBox='0 0 400 225'%3E%3Crect width='400' height='225' fill='%23111'/%3E%3Cpath d='M160,90 L160,135 L200,112.5 Z' fill='%23333'/%3E%3C/svg%3E">
                        <source src="/static/videos/{video}" type="video/{file_ext.lower()}">
                        Your browser does not support the video tag.
                    </video>
                </div>
                <div class="video-info">
                    <div class="file-size">
                        <i class="fas fa-hdd"></i>
                        <span>{file_size_display}</span>
                    </div>
                    <div class="file-type">
                        {file_ext}
                    </div>
                </div>
            </div>
"""

    total_size_display = f"{total_size / (1024 * 1024):.1f} MB"
    
    html += f"""
        </div>
        
        <div class="footer">
            <p>Generated automatically with ❤️ | {len(videos)} videos ({total_size_display})</p>
        </div>
    </div>

    <script>
        // Auto-refresh every 30 seconds to check for new videos
        setTimeout(() => {{
            window.location.reload();
        }}, 30000);

        // Add loading states to videos
        document.addEventListener('DOMContentLoaded', function() {{
            const videos = document.querySelectorAll('video');
            
            videos.forEach(video => {{
                video.addEventListener('loadstart', function() {{
                    this.style.opacity = '0.7';
                }});
                
                video.addEventListener('canplay', function() {{
                    this.style.opacity = '1';
                }});
                
                // Add click to play/pause
                video.addEventListener('click', function() {{
                    if (this.paused) {{
                        this.play();
                    }} else {{
                        this.pause();
                    }}
                }});
            }});
        }});
    </script>
</body>
</html>
"""

    return html

@app.route('/')
def index():
    return generate_video_gallery()

@app.route('/health')
def health():
    return json.dumps({"status": "healthy"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)