# 跨境电商运营实战模拟系统

下面是一个基于您提供的跨境电商运营实战模拟方案的网页实现。这个系统将模拟整个跨境电商运营流程，包括团队管理、产品选择、运营决策和结果反馈。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>跨境电商运营实战模拟系统</title>
    <style>
        :root {
            --primary-color: #2563eb;
            --secondary-color: #1e40af;
            --accent-color: #3b82f6;
            --light-color: #f8fafc;
            --dark-color: #1e293b;
            --success-color: #10b981;
            --warning-color: #f59e0b;
            --danger-color: #ef4444;
            --border-radius: 8px;
            --box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background-color: #f1f5f9;
            color: var(--dark-color);
            line-height: 1.6;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        header {
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: white;
            padding: 2rem 0;
            border-radius: var(--border-radius);
            margin-bottom: 2rem;
            box-shadow: var(--box-shadow);
            text-align: center;
        }
        
        h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }
        
        h2 {
            font-size: 1.8rem;
            margin: 1.5rem 0 1rem;
            color: var(--secondary-color);
            border-bottom: 2px solid var(--accent-color);
            padding-bottom: 0.5rem;
        }
        
        h3 {
            font-size: 1.4rem;
            margin: 1.2rem 0 0.8rem;
            color: var(--primary-color);
        }
        
        .card {
            background: white;
            border-radius: var(--border-radius);
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: var(--box-shadow);
            transition: transform 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-5px);
        }
        
        .dashboard {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }
        
        .dashboard-item {
            background: white;
            border-radius: var(--border-radius);
            padding: 1.5rem;
            box-shadow: var(--box-shadow);
            text-align: center;
        }
        
        .dashboard-item h3 {
            color: var(--secondary-color);
            margin-bottom: 0.5rem;
        }
        
        .value {
            font-size: 2rem;
            font-weight: bold;
            color: var(--primary-color);
        }
        
        .team-section {
            display: flex;
            flex-wrap: wrap;
            gap: 1.5rem;
            margin-bottom: 2rem;
        }
        
        .team-card {
            flex: 1 1 300px;
            background: white;
            border-radius: var(--border-radius);
            padding: 1.5rem;
            box-shadow: var(--box-shadow);
        }
        
        .team-card h3 {
            color: var(--secondary-color);
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid #e2e8f0;
        }
        
        .product-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }
        
        .product-card {
            background: white;
            border-radius: var(--border-radius);
            padding: 1.5rem;
            box-shadow: var(--box-shadow);
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .product-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        }
        
        .product-card.selected {
            border: 2px solid var(--primary-color);
            background-color: #f0f9ff;
        }
        
        .product-card h4 {
            color: var(--secondary-color);
            margin-bottom: 0.8rem;
        }
        
        .progress-container {
            margin: 2rem 0;
        }
        
        .progress-bar {
            height: 10px;
            background-color: #e2e8f0;
            border-radius: 5px;
            overflow: hidden;
            margin-bottom: 0.5rem;
        }
        
        .progress {
            height: 100%;
            background: linear-gradient(90deg, var(--primary-color), var(--accent-color));
            border-radius: 5px;
            transition: width 0.5s ease;
        }
        
        .phase-container {
            display: flex;
            justify-content: space-between;
            margin-top: 1rem;
        }
        
        .phase {
            text-align: center;
            flex: 1;
            padding: 0.5rem;
        }
        
        .phase.active {
            font-weight: bold;
            color: var(--primary-color);
        }
        
        .task-list {
            list-style-type: none;
            margin: 1rem 0;
        }
        
        .task-item {
            padding: 0.8rem;
            margin-bottom: 0.5rem;
            background-color: #f8fafc;
            border-radius: var(--border-radius);
            border-left: 4px solid var(--accent-color);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .task-item.completed {
            background-color: #d1fae5;
            border-left-color: var(--success-color);
        }
        
        .btn {
            display: inline-block;
            background-color: var(--primary-color);
            color: white;
            padding: 0.7rem 1.5rem;
            border: none;
            border-radius: var(--border-radius);
            cursor: pointer;
            font-weight: 600;
            transition: background-color 0.3s ease;
            text-decoration: none;
        }
        
        .btn:hover {
            background-color: var(--secondary-color);
        }
        
        .btn-success {
            background-color: var(--success-color);
        }
        
        .btn-success:hover {
            background-color: #059669;
        }
        
        .btn-warning {
            background-color: var(--warning-color);
        }
        
        .btn-warning:hover {
            background-color: #d97706;
        }
        
        .btn-danger {
            background-color: var(--danger-color);
        }
        
        .btn-danger:hover {
            background-color: #dc2626;
        }
        
        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.5);
            z-index: 1000;
            justify-content: center;
            align-items: center;
        }
        
        .modal-content {
            background-color: white;
            border-radius: var(--border-radius);
            padding: 2rem;
            width: 90%;
            max-width: 600px;
            max-height: 80vh;
            overflow-y: auto;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        }
        
        .close-btn {
            float: right;
            font-size: 1.5rem;
            cursor: pointer;
            color: #64748b;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 1rem 0;
        }
        
        th, td {
            padding: 0.8rem;
            text-align: left;
            border-bottom: 1px solid #e2e8f0;
        }
        
        th {
            background-color: #f1f5f9;
            color: var(--secondary-color);
        }
        
        tr:hover {
            background-color: #f8fafc;
        }
        
        .form-group {
            margin-bottom: 1.2rem;
        }
        
        label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 600;
            color: var(--dark-color);
        }
        
        input, select, textarea {
            width: 100%;
            padding: 0.8rem;
            border: 1px solid #cbd5e1;
            border-radius: var(--border-radius);
            font-size: 1rem;
        }
        
        textarea {
            min-height: 120px;
            resize: vertical;
        }
        
        .alert {
            padding: 1rem;
            border-radius: var(--border-radius);
            margin-bottom: 1rem;
        }
        
        .alert-success {
            background-color: #d1fae5;
            color: #065f46;
            border: 1px solid #a7f3d0;
        }
        
        .alert-warning {
            background-color: #fef3c7;
            color: #92400e;
            border: 1px solid #fcd34d;
        }
        
        .alert-danger {
            background-color: #fee2e2;
            color: #991b1b;
            border: 1px solid #fca5a5;
        }
        
        .tab-container {
            margin: 2rem 0;
        }
        
        .tabs {
            display: flex;
            border-bottom: 1px solid #cbd5e1;
            margin-bottom: 1rem;
        }
        
        .tab {
            padding: 0.8rem 1.5rem;
            cursor: pointer;
            border-bottom: 3px solid transparent;
        }
        
        .tab.active {
            border-bottom-color: var(--primary-color);
            color: var(--primary-color);
            font-weight: 600;
        }
        
        .tab-content {
            display: none;
        }
        
        .tab-content.active {
            display: block;
        }
        
        @media (max-width: 768px) {
            .dashboard {
                grid-template-columns: 1fr;
            }
            
            .team-section {
                flex-direction: column;
            }
            
            .product-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>跨境电商运营实战模拟系统</h1>
            <p>培养数据驱动决策与创业者思维的实战平台</p>
        </header>
        
        <div class="dashboard">
            <div class="dashboard-item">
                <h3>当前资金</h3>
                <div class="value">¥50,000</div>
                <p>初始启动资金</p>
            </div>
            <div class="dashboard-item">
                <h3>当前季度</h3>
                <div class="value">第1季度</div>
                <p>共4个季度</p>
            </div>
            <div class="dashboard-item">
                <h3>团队排名</h3>
                <div class="value">第3名</div>
                <p>共8个团队</p>
            </div>
            <div class="dashboard-item">
                <h3>产品数量</h3>
                <div class="value">1款</div>
                <p>已上架产品</p>
            </div>
        </div>
        
        <div class="card">
            <h2>模拟进度</h2>
            <div class="progress-container">
                <div class="progress-bar">
                    <div class="progress" style="width: 25%"></div>
                </div>
                <div class="phase-container">
                    <div class="phase active">启动与奠基期</div>
                    <div class="phase">上线与爬升期</div>
                    <div class="phase">稳定增长期</div>
                    <div class="phase">规模化与风控期</div>
                </div>
            </div>
            
            <h3>当前任务 (第1-3周)</h3>
            <ul class="task-list">
                <li class="task-item">
                    <span>任务1：市场调研与选品决策</span>
                    <button class="btn btn-success">已完成</button>
                </li>
                <li class="task-item">
                    <span>任务2：供应链准备与成本精算</span>
                    <button class="btn btn-warning">进行中</button>
                </li>
                <li class="task-item">
                    <span>任务3：品牌化建设与Listing优化</span>
                    <button class="btn">未开始</button>
                </li>
            </ul>
        </div>
        
        <div class="card">
            <h2>团队信息</h2>
            <div class="team-section">
                <div class="team-card">
                    <h3>团队A - 运营概况</h3>
                    <p><strong>团队成员:</strong> 4人</p>
                    <p><strong>当前产品:</strong> 运动耳机</p>
                    <p><strong>当前资金:</strong> ¥47,200</p>
                    <p><strong>库存数量:</strong> 300件</p>
                    <p><strong>已完成订单:</strong> 45单</p>
                    <button class="btn" style="margin-top: 1rem;">查看详细报告</button>
                </div>
                
                <div class="team-card">
                    <h3>关键绩效指标</h3>
                    <p><strong>转化率:</strong> 12.5%</p>
                    <p><strong>广告ACOS:</strong> 28%</p>
                    <p><strong>平均星级:</strong> 4.3★</p>
                    <p><strong>库存周转率:</strong> 1.2</p>
                    <p><strong>净利润率:</strong> 22%</p>
                    <button class="btn" style="margin-top: 1rem;">优化策略</button>
                </div>
            </div>
        </div>
        
        <div class="card">
            <h2>产品选择</h2>
            <p>选择您要销售的产品类别和具体产品：</p>
            
            <div class="tab-container">
                <div class="tabs">
                    <div class="tab active" data-tab="electronics">电子产品</div>
                    <div class="tab" data-tab="clothing">服装</div>
                    <div class="tab" data-tab="beauty">美妆</div>
                </div>
                
                <div class="tab-content active" id="electronics">
                    <div class="product-grid">
                        <div class="product-card selected">
                            <h4>运动耳机</h4>
                            <p><strong>目标客群:</strong> 健身爱好者、跑步者</p>
                            <p><strong>竞争程度:</strong> ★★★★☆</p>
                            <p><strong>机会点:</strong> 防汗防水、耳挂设计、环境音模式</p>
                            <p><strong>核心成本:</strong> BOM成本、认证费用、研发费用</p>
                            <button class="btn" style="margin-top: 0.8rem;">选择此产品</button>
                        </div>
                        
                        <div class="product-card">
                            <h4>大容量快充充电宝</h4>
                            <p><strong>目标客群:</strong> 重度手机用户、短途旅行者</p>
                            <p><strong>竞争程度:</strong> ★★★★☆</p>
                            <p><strong>机会点:</strong> 20000mAh+容量、多种快充协议、数显屏</p>
                            <p><strong>核心成本:</strong> 电芯成本、PCBA板、认证费用</p>
                            <button class="btn" style="margin-top: 0.8rem;">选择此产品</button>
                        </div>
                        
                        <div class="product-card">
                            <h4>电竞游戏本</h4>
                            <p><strong>目标客群:</strong> 硬核游戏玩家、学生</p>
                            <p><strong>竞争程度:</strong> ★★★★★</p>
                            <p><strong>机会点:</strong> 高性能与散热平衡、高刷新率屏幕、个性化设计</p>
                            <p><strong>核心成本:</strong> BOM成本、研发费用、模具费用</p>
                            <button class="btn" style="margin-top: 0.8rem;">选择此产品</button>
                        </div>
                    </div>
                </div>
                
                <div class="tab-content" id="clothing">
                    <div class="product-grid">
                        <div class="product-card">
                            <h4>法式风格设计感衬衫</h4>
                            <p><strong>目标客群:</strong> 追求个性、厌烦爆款的年轻女性</p>
                            <p><strong>竞争程度:</strong> ★★★★☆</p>
                            <p><strong>机会点:</strong> 独特设计元素、强烈风格叙事、社交媒体种草</p>
                            <p><strong>核心成本:</strong> 面料成本、加工费、设计开发费</p>
                            <button class="btn" style="margin-top: 0.8rem;">选择此产品</button>
                        </div>
                        
                        <div class="product-card">
                            <h4>高品质基础款T恤</h4>
                            <p><strong>目标客群:</strong> 注重质感的成熟男性、上班族</p>
                            <p><strong>竞争程度:</strong> ★★★★★</p>
                            <p><strong>机会点:</strong> 面料升级、工艺细节、合身版型</p>
                            <p><strong>核心成本:</strong> 面料成本、加工费、库存持有成本</p>
                            <button class="btn" style="margin-top: 0.8rem;">选择此产品</button>
                        </div>
                    </div>
                </div>
                
                <div class="tab-content" id="beauty">
                    <div class="product-grid">
                        <div class="product-card">
                            <h4>高浓度原型VC精华液</h4>
                            <p><strong>目标客群:</strong> 成分党、资深护肤爱好者</p>
                            <p><strong>竞争程度:</strong> ★★★★☆</p>
                            <p><strong>机会点:</strong> 高浓度和pH值、日间抗氧化、早C晚A套餐</p>
                            <p><strong>核心成本:</strong> 活性成分成本、包材成本、认证测试成本</p>
                            <button class="btn" style="margin-top: 0.8rem;">选择此产品</button>
                        </div>
                        
                        <div class="product-card">
                            <h4>极细头液体眉笔</h4>
                            <p><strong>目标客群:</strong> 化妆高手、追求精致妆效者</p>
                            <p><strong>竞争程度:</strong> ★★★★☆</p>
                            <p><strong>机会点:</strong> 根根分明的毛流、野生眉效果、不易晕染</p>
                            <p><strong>核心成本:</strong> 笔芯与笔头成本、包装与模具成本、品控成本</p>
                            <button class="btn" style="margin-top: 0.8rem;">选择此产品</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="card">
            <h2>决策与行动</h2>
            <div class="form-group">
                <label for="decision-type">决策类型</label>
                <select id="decision-type">
                    <option value="">请选择决策类型</option>
                    <option value="market-research">市场调研</option>
                    <option value="supplier-selection">供应商选择</option>
                    <option value="listing-optimization">Listing优化</option>
                    <option value="ad-campaign">广告投放</option>
                    <option value="inventory-management">库存管理</option>
                    <option value="risk-response">风险应对</option>
                </select>
            </div>
            
            <div class="form-group">
                <label for="decision-details">决策详情</label>
                <textarea id="decision-details" placeholder="请详细描述您的决策内容和理由..."></textarea>
            </div>
            
            <div class="form-group">
                <label for="budget-allocation">预算分配 (元)</label>
                <input type="number" id="budget-allocation" placeholder="请输入预算金额">
            </div>
            
            <button class="btn">提交决策</button>
        </div>
        
        <div class="card">
            <h2>系统反馈与市场模拟结果</h2>
            <div class="alert alert-success">
                <strong>第3周反馈:</strong> 选品通过。市场模拟：运动耳机上市后，预计月均自然需求为200单，但竞争激烈。
            </div>
            
            <div class="alert alert-warning">
                <strong>第6周反馈:</strong> Listing A+得分高。市场模拟：上架首周，因无评论，转化率仅为5%。
            </div>
            
            <table>
                <thead>
                    <tr>
                        <th>决策周期</th>
                        <th>团队行动方案</th>
                        <th>系统/裁判反馈</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>第3周结束</td>
                        <td>《选品分析报告》、《产品成本核算表》</td>
                        <td>选品通过。市场模拟：产品A上市后，预计月均自然需求为200单，但竞争激烈。</td>
                    </tr>
                    <tr>
                        <td>第6周结束</td>
                        <td>Listing文案、主图、首批发货计划</td>
                        <td>Listing A+得分高。市场模拟：上架首周，因无评论，转化率仅为5%。</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- 产品详情模态框 -->
    <div class="modal" id="product-modal">
        <div class="modal-content">
            <span class="close-btn">&times;</span>
            <h2 id="modal-product-title">产品详情</h2>
            <div id="modal-product-content">
                <!-- 产品详情内容将通过JavaScript动态加载 -->
            </div>
        </div>
    </div>

    <script>
        // 标签切换功能
        document.querySelectorAll('.tab').forEach(tab => {
            tab.addEventListener('click', () => {
                // 移除所有标签和内容的active类
                document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
                document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
                
                // 为当前标签和对应内容添加active类
                tab.classList.add('active');
                const tabId = tab.getAttribute('data-tab');
                document.getElementById(tabId).classList.add('active');
            });
        });
        
        // 产品选择功能
        document.querySelectorAll('.product-card').forEach(card => {
            card.addEventListener('click', (e) => {
                if (e.target.tagName === 'BUTTON') {
                    // 移除所有产品的selected类
                    document.querySelectorAll('.product-card').forEach(c => {
                        c.classList.remove('selected');
                    });
                    
                    // 为当前产品添加selected类
                    card.classList.add('selected');
                    
                    // 显示成功消息
                    alert('产品选择成功！');
                }
            });
        });
        
        // 模态框功能
        const modal = document.getElementById('product-modal');
        const closeBtn = document.querySelector('.close-btn');
        
        closeBtn.addEventListener('click', () => {
            modal.style.display = 'none';
        });
        
        window.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.style.display = 'none';
            }
        });
        
        // 任务完成状态切换
        document.querySelectorAll('.task-item button').forEach(button => {
            button.addEventListener('click', function() {
                const taskItem = this.parentElement;
                
                if (this.classList.contains('btn-success')) {
                    this.textContent = '进行中';
                    this.classList.remove('btn-success');
                    this.classList.add('btn-warning');
                    taskItem.classList.remove('completed');
                } else if (this.classList.contains('btn-warning')) {
                    this.textContent = '未开始';
                    this.classList.remove('btn-warning');
                    taskItem.classList.remove('completed');
                } else {
                    this.textContent = '已完成';
                    this.classList.add('btn-success');
                    taskItem.classList.add('completed');
                }
            });
        });
        
        // 模拟提交决策
        document.querySelector('.card:last-of-type .btn').addEventListener('click', function() {
            const decisionType = document.getElementById('decision-type').value;
            const decisionDetails = document.getElementById('decision-details').value;
            const budget = document.getElementById('budget-allocation').value;
            
            if (!decisionType || !decisionDetails || !budget) {
                alert('请填写完整的决策信息！');
                return;
            }
            
            alert('决策已提交！系统将在下一周期反馈结果。');
            
            // 清空表单
            document.getElementById('decision-type').value = '';
            document.getElementById('decision-details').value = '';
            document.getElementById('budget-allocation').value = '';
        });
    </script>
</body>
</html>
```

## 系统功能说明

这个跨境电商运营实战模拟系统具有以下核心功能：

1. **模拟概览仪表板**：显示当前资金、季度、团队排名和产品数量等关键信息

2. **模拟进度跟踪**：可视化展示四个阶段的进度和当前任务状态

3. **团队信息管理**：展示团队运营概况和关键绩效指标

4. **产品选择系统**：
   - 按电子产品、服装和美妆三大类分类
   - 每个产品卡片包含目标客群、竞争程度、机会点和核心成本信息
   - 支持产品选择和切换

5. **决策与行动提交**：
   - 支持多种决策类型选择
   - 提供决策详情和预算分配输入
   - 提交决策后等待系统反馈

6. **系统反馈机制**：
   - 显示历史反馈和模拟结果
   - 以表格形式展示决策周期、团队行动和系统反馈

## 使用说明

1. 查看当前模拟进度和待完成任务
2. 选择适合的产品类别和具体产品
3. 根据当前阶段提交相应的决策和行动方案
4. 查看系统反馈并根据反馈调整策略
5. 跟踪关键绩效指标，优化运营策略

这个系统可以帮助学员在模拟环境中实践跨境电商运营的全流程，培养数据驱动决策和创业者思维。
