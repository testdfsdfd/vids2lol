import os
from flask import Flask
import json

app = Flask(__name__)

def generate_video_gallery():
    # This would be replaced with your actual Google Drive video data
    # For now, using sample data structure
    google_drive_videos = [
        {
        "name": "CBVideo",
        "drive_url": "https://drive.google.com/file/d/1ppUDD-fDzl5q1OTJjmaKEX6uBqNRR_3B/view?usp=sharing",
        "embed_url": "https://drive.google.com/file/d/1ppUDD-fDzl5q1OTJjmaKEX6uBqNRR_3B/preview",
        "file_type": "MP4",
        "file_size": "1.58 GB",
        "duration": "2:40:22",
        "last_modified": "2025-10-27"
    },
    {
        "name": "CBVideo",
        "drive_url": "https://drive.google.com/file/d//view?usp=sharing",
        "embed_url": "https://drive.google.com/file/d//preview",
        "file_type": "MP4",
        "file_size": "1.54 GB",
        "duration": "2:40:22",
        "last_modified": "2025-10-27"
    },
        {
        "name": "CBVideo",
        "drive_url": "https://drive.google.com/file/d/1qXgkD8N_hkKDn6PvrlQepaY4fDzSo8NQ/view?usp=sharing",
        "embed_url": "https://drive.google.com/file/d/1qXgkD8N_hkKDn6PvrlQepaY4fDzSo8NQ/preview",
        "file_type": "MP4",
        "file_size": "1.49 GB",
        "duration": "2:26:29",
        "last_modified": "2025-10-27"
    },
    {
        "name": "CBVideo",
        "drive_url": "https://drive.google.com/file/d//view?usp=sharing",
        "embed_url": "https://drive.google.com/file/d//preview",
        "file_type": "MP4",
        "file_size": "1.32 GB",
        "duration": "2:40:22",
        "last_modified": "2025-10-27"
    },
    {
        "name": "CBVideo",
        "drive_url": "https://drive.google.com/file/d/1z0u6M_AOy9tXYCLRimOaRvZqEvKnZF1O/view?usp=sharing",
        "embed_url": "https://drive.google.com/file/d/1z0u6M_AOy9tXYCLRimOaRvZqEvKnZF1O/preview",
        "file_type": "MP4",
        "file_size": "1.19 GB",
        "duration": "1:57:12",
        "last_modified": "2025-10-27"
    },
    {
        "name": "CBVideo",
        "drive_url": "https://drive.google.com/file/d/1NkEGEjByxjvPhlQ5zrvM9iuIALeUDSUB/view?usp=sharing",
        "embed_url": "https://drive.google.com/file/d/1NkEGEjByxjvPhlQ5zrvM9iuIALeUDSUB/preview",
        "file_type": "MP4",
        "file_size": "1.03 GB",
        "duration": "1:44:24",
        "last_modified": "2025-10-27"
    },
    {
    
        "name": "CBVideo",
        "drive_url": "https://drive.google.com/file/d/1e6_h4XyeRuesJZG7KKhyhNLf0sAVUPbl/view?usp=sharing",
        "embed_url": "https://drive.google.com/file/d/1e6_h4XyeRuesJZG7KKhyhNLf0sAVUPbl/preview",
        "file_type": "MP4",
        "file_size": "789.6 MB",
        "duration": "1:28:14",
        "last_modified": "2025-10-27"
    },
    {
    
        "name": "CBVideo",
        "drive_url": "https://drive.google.com/file/d/1dcykIhsz9ioMO83K8B7kIoFhf8hLnqj2/view?usp=sharing",
        "embed_url": "https://drive.google.com/file/d/1dcykIhsz9ioMO83K8B7kIoFhf8hLnqj2/preview",
        "file_type": "MP4",
        "file_size": "749.4 MB",
        "duration": "1:08:55",
        "last_modified": "2025-10-27"
    },
    {
    
        "name": "CBVideo",
        "drive_url": "https://drive.google.com/file/d/1nak73al-GRhtZM5MKbGSkSmm6u0in7-w/view?usp=sharing",
        "embed_url": "https://drive.google.com/file/d/1nak73al-GRhtZM5MKbGSkSmm6u0in7-w/preview",
        "file_type": "MP4",
        "file_size": "698.3 MB",
        "duration": "1:06:58",
        "last_modified": "2025-10-27"
    },
    {
    
        "name": "CBVideo",
        "drive_url": "https://drive.google.com/file/d/13fe6B8GRspvZnSAB0PSebj7D3AX19n9v/view?usp=sharing",
        "embed_url": "https://drive.google.com/file/d/13fe6B8GRspvZnSAB0PSebj7D3AX19n9v/preview",
        "file_type": "MP4",
        "file_size": "537.2 MB",
        "duration": "1:02:18",
        "last_modified": "2025-10-27"
    },
    {
    
        "name": "CBVideo",
        "drive_url": "https://drive.google.com/file/d/1wMR3AmWzw762bZmAsnjWt5hQ1NPk_wAc/view?usp=sharing",
        "embed_url": "https://drive.google.com/file/d/1wMR3AmWzw762bZmAsnjWt5hQ1NPk_wAc/preview",
        "file_type": "MP4",
        "file_size": "453.4 MB",
        "duration": "51:06",
        "last_modified": "2025-10-27"
    },
    {
    
        "name": "CBVideo",
        "drive_url": "https://drive.google.com/file/d//view?usp=sharing",
        "embed_url": "https://drive.google.com/file/d//preview",
        "file_type": "MP4",
        "file_size": "353.4 MB",
        "duration": "51:06",
        "last_modified": "2025-10-27"
    },
    {
        "name": "CBVideo",
        "drive_url": "https://drive.google.com/file/d/17bvnPWaKmB-WwXb5OpDZszxFTX7axLIR/view?usp=sharing",
        "embed_url": "https://drive.google.com/file/d/17bvnPWaKmB-WwXb5OpDZszxFTX7axLIR/preview",
        "file_type": "MP4",
        "file_size": "343.3 MB",
        "duration": "25:56",
        "last_modified": "2025-10-27"
    },
    {
        "name": "CBVideo",
        "drive_url": "https://drive.google.com/file/d/1Hq-U0Z59VZoSGidXPKuTd35jUHkEX3uB/view?usp=sharing",
        "embed_url": "https://drive.google.com/file/d/1Hq-U0Z59VZoSGidXPKuTd35jUHkEX3uB/preview",
        "file_type": "MP4",
        "file_size": "316.3 MB",
        "duration": "29:02",
        "last_modified": "2025-10-27"
    },
    {
    
        "name": "CBVideo",
        "drive_url": "https://drive.google.com/file/d/1Wi70PEz0VMwJysZdcU8Qphrm4rG7HEc1/view?usp=sharing",
        "embed_url": "https://drive.google.com/file/d/1Wi70PEz0VMwJysZdcU8Qphrm4rG7HEc1/preview",
        "file_type": "MP4",
        "file_size": "313.9 MB",
        "duration": "8:27",
        "last_modified": "2025-10-27"
    },
    {
        "name": "Porn",
        "drive_url": "https://drive.google.com/file/d/1LUg3tERzpkm30LEg7hwrK-rg71oglKNE/view?usp=sharing",
        "embed_url": "https://drive.google.com/file/d/1LUg3tERzpkm30LEg7hwrK-rg71oglKNE/preview",
        "file_type": "MP4",
        "file_size": "243.3 MB",
        "duration": "9:17",
        "last_modified": "2025-10-27"
    },
    {
        "name": "Porn",
        "drive_url": "https://drive.google.com/file/d/1KbS-oAp-YJvyXPCGYc_caKVYT3bfljo1/view?usp=sharing",
        "embed_url": "https://drive.google.com/file/d/1KbS-oAp-YJvyXPCGYc_caKVYT3bfljo1/preview",
        "file_type": "MP4",
        "file_size": "194 MB",
        "duration": "8:54",
        "last_modified": "2025-10-27"
    },
    {
        "name": "Porn",
        "drive_url": "https://drive.google.com/file/d/1bY010t2PB85dqIy6hR4mHrw1f4BeJ2y6/view?usp=sharing",
        "embed_url": "https://drive.google.com/file/d/1bY010t2PB85dqIy6hR4mHrw1f4BeJ2y6/preview",
        "file_type": "MP4",
        "file_size": "174.6 MB",
        "duration": "5:11",
        "last_modified": "2025-10-27"
    },
    {
        "name": "Porn",
        "drive_url": "https://drive.google.com/file/d//view?usp=sharing",
        "embed_url": "https://drive.google.com/file/d//preview",
        "file_type": "MP4",
        "file_size": "169.1 MB",
        "duration": "8:54",
        "last_modified": "2025-10-27"
    },
    {
        "name": "Porn",
        "drive_url": "https://drive.google.com/file/d//view?usp=sharing",
        "embed_url": "https://drive.google.com/file/d//preview",
        "file_type": "MP4",
        "file_size": "111.1 MB",
        "duration": "8:54",
        "last_modified": "2025-10-27"
    },
    ]


    # Build HTML with modern design
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Google Drive Video Gallery</title>
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
            max-width: 1400px;
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

        .video-table-container {{
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 2rem;
            border: 1px solid rgba(255, 255, 255, 0.1);
            margin-top: 2rem;
            overflow-x: auto;
        }}

        .video-table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 1rem;
        }}

        .video-table th {{
            background: rgba(0, 255, 255, 0.1);
            padding: 1rem;
            text-align: left;
            color: #00ffff;
            font-weight: 600;
            border-bottom: 2px solid rgba(0, 255, 255, 0.3);
        }}

        .video-table td {{
            padding: 1rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }}

        .video-table tr:hover {{
            background: rgba(255, 255, 255, 0.05);
        }}

        .video-preview {{
            width: 300px;
            height: 169px;
            border-radius: 10px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            overflow: hidden;
        }}

        .video-preview iframe {{
            width: 100%;
            height: 100%;
            border: none;
        }}

        .video-info {{
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }}

        .video-name {{
            font-weight: 600;
            color: #00ffff;
            font-size: 1.1rem;
        }}

        .video-meta {{
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
            font-size: 0.9rem;
            color: #8892b0;
        }}

        .meta-item {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .action-buttons {{
            display: flex;
            gap: 0.5rem;
        }}

        .btn {{
            padding: 0.5rem 1rem;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            transition: all 0.3s ease;
            font-size: 0.9rem;
        }}

        .btn-primary {{
            background: rgba(0, 255, 255, 0.2);
            color: #00ffff;
            border: 1px solid rgba(0, 255, 255, 0.3);
        }}

        .btn-primary:hover {{
            background: rgba(0, 255, 255, 0.3);
            transform: translateY(-2px);
        }}

        .btn-secondary {{
            background: rgba(255, 255, 255, 0.1);
            color: #ffffff;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }}

        .btn-secondary:hover {{
            background: rgba(255, 255, 255, 0.2);
            transform: translateY(-2px);
        }}

        .footer {{
            text-align: center;
            margin-top: 4rem;
            color: #8892b0;
            padding: 2rem 0;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }}

        @media (max-width: 768px) {{
            .video-table-container {{
                padding: 1rem;
            }}
            
            .video-table th, 
            .video-table td {{
                padding: 0.5rem;
            }}
            
            .header h1 {{
                font-size: 2.5rem;
            }}
            
            .container {{
                padding: 1rem;
            }}
            
            .video-preview {{
                width: 200px;
                height: 113px;
            }}
        }}

        /* Loading animation */
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(30px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .video-table tr {{
            animation: fadeIn 0.6s ease forwards;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1><i class="fab fa-google-drive"></i> Google Drive Videos</h1>
            <p>Your video collection from Google Drive</p>
            <div class="stats">
                <div class="stat-item">
                    <i class="fas fa-video"></i> {len(google_drive_videos)} videos
                </div>
                <div class="stat-item">
                    <i class="fas fa-cloud"></i> Google Drive
                </div>
                <div class="stat-item">
                    <i class="fas fa-sync-alt"></i> Auto-refresh
                </div>
            </div>
        </div>

        <div class="video-table-container">
            <table class="video-table">
                <thead>
                    <tr>
                        <th>Video Preview</th>
                        <th>Video Information</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
"""

    for video in google_drive_videos:
        html += f"""
                    <tr>
                        <td>
                            <div class="video-preview">
                                <iframe src="{video['embed_url']}" 
                                        allow="autoplay; encrypted-media" 
                                        allowfullscreen>
                                </iframe>
                            </div>
                        </td>
                        <td>
                            <div class="video-info">
                                <div class="video-name">{video['name']}</div>
                                <div class="video-meta">
                                    <div class="meta-item">
                                        <i class="fas fa-file"></i>
                                        <span>{video['file_type']}</span>
                                    </div>
                                    <div class="meta-item">
                                        <i class="fas fa-hdd"></i>
                                        <span>{video['file_size']}</span>
                                    </div>
                                    <div class="meta-item">
                                        <i class="fas fa-clock"></i>
                                        <span>{video['duration']}</span>
                                    </div>
                                    <div class="meta-item">
                                        <i class="fas fa-calendar"></i>
                                        <span>{video['last_modified']}</span>
                                    </div>
                                </div>
                            </div>
                        </td>
                        <td>
                            <div class="action-buttons">
                                <a href="{video['drive_url']}" target="_blank" class="btn btn-primary">
                                    <i class="fas fa-external-link-alt"></i>
                                    Open in Drive
                                </a>
                                <button class="btn btn-secondary" onclick='playVideo("{video['embed_url']}")'>
                                    <i class="fas fa-play"></i>
                                    Play
                                </button>
                            </div>
                        </td>
                    </tr>
"""

    html += f"""
                </tbody>
            </table>
        </div>
        
        <div class="footer">
            <p>Powered by Google Drive ❤️ | {len(google_drive_videos)} videos loaded</p>
        </div>
    </div>

    <script>
        function playVideo(embedUrl) {{
            // Open video in a new window or modal for better viewing
            window.open(embedUrl, '_blank', 'width=800,height=600');
        }}

        // Auto-refresh every 60 seconds
        setTimeout(() => {{
            window.location.reload();
        }}, 60000);

        // Add click handlers for better UX
        document.addEventListener('DOMContentLoaded', function() {{
            const videoRows = document.querySelectorAll('.video-table tbody tr');
            
            videoRows.forEach(row => {{
                row.addEventListener('click', function(e) {{
                    // Don't trigger if clicking on buttons
                    if (!e.target.closest('.btn')) {{
                        const iframe = this.querySelector('iframe');
                        if (iframe) {{
                            const embedUrl = iframe.src;
                            playVideo(embedUrl);
                        }}
                    }}
                }});
                
                row.style.cursor = 'pointer';
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
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
