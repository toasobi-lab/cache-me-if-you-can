# Contributing to Cache Me If You Can

Thank you for your interest in contributing to this educational Redis caching project! This project is designed to help people learn about caching patterns, Docker orchestration, and microservice architecture.

## 🎯 Project Goals

This project aims to:
- Provide a hands-on learning experience for Redis caching
- Demonstrate cache-aside patterns in a realistic microservice environment
- Show real-time performance differences between cached and uncached requests
- Serve as a template for similar educational projects

## 🚀 Getting Started

### Prerequisites
- Docker (20.10+) and Docker Compose (2.0+)
- Git
- Basic knowledge of Python, JavaScript, or Docker

### Local Development Setup
1. Fork the repository
2. Clone your fork: `git clone https://github.com/your-username/cache-me-if-you-can.git`
3. Navigate to the project: `cd cache-me-if-you-can`
4. Start the services: `docker compose up -d --build`
5. Test the setup: Visit http://localhost:3000

## 🛠️ How to Contribute

### Types of Contributions Welcome

#### 🐛 Bug Fixes
- Fix issues with service startup or connectivity
- Resolve UI/UX problems
- Address performance issues
- Fix documentation errors

#### ✨ Feature Enhancements
- Add new caching strategies (write-through, write-behind, etc.)
- Implement additional metrics and monitoring
- Enhance the frontend UI/UX
- Add new API endpoints
- Improve error handling

#### 📚 Documentation
- Improve setup instructions
- Add troubleshooting guides
- Create tutorial content
- Add code comments and examples
- Translate documentation

#### 🧪 Testing & Quality
- Add unit tests for backend services
- Create integration tests
- Add performance benchmarks
- Improve error handling
- Add health checks

### Contribution Process

1. **Check existing issues** - Look for related issues or create a new one
2. **Fork and branch** - Create a feature branch from `main`
3. **Make changes** - Follow the coding standards below
4. **Test thoroughly** - Ensure all services work correctly
5. **Update documentation** - Update README if needed
6. **Submit PR** - Create a pull request with clear description

## 📝 Coding Standards

### Backend (Python/FastAPI)
- Follow PEP 8 style guidelines
- Use type hints for function parameters and return values
- Add docstrings for functions and classes
- Handle errors gracefully with appropriate HTTP status codes
- Use async/await for database and cache operations

### Frontend (Astro/JavaScript)
- Use consistent indentation (2 spaces)
- Follow modern JavaScript practices (ES6+)
- Use semantic HTML elements
- Maintain responsive design principles
- Add comments for complex logic

### Docker & Infrastructure
- Use multi-stage builds where appropriate
- Include health checks for services
- Use named volumes with descriptive names
- Document environment variables
- Follow security best practices

## 🧪 Testing Your Changes

### Manual Testing Checklist
- [ ] All services start successfully: `docker compose up -d --build`
- [ ] Frontend loads at http://localhost:3000
- [ ] API documentation accessible at http://localhost:8000/docs
- [ ] Product lookup works (test cache miss and hit)
- [ ] Cache statistics display correctly
- [ ] Cache clear functionality works
- [ ] pgAdmin connects automatically
- [ ] Redis Commander shows cached data

### Performance Testing
- Test cache hit/miss performance differences
- Verify memory usage remains reasonable
- Check for any memory leaks during extended use
- Ensure services recover gracefully from failures

## 📋 Pull Request Guidelines

### PR Title Format
Use descriptive titles with prefixes:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `refactor:` for code refactoring
- `test:` for adding tests
- `chore:` for maintenance tasks

### PR Description Template
```markdown
## Description
Brief description of changes made.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Refactoring
- [ ] Other (please describe)

## Testing
- [ ] Manual testing completed
- [ ] All services start successfully
- [ ] Frontend functionality verified
- [ ] Performance impact assessed

## Screenshots (if applicable)
Add screenshots for UI changes.

## Additional Notes
Any additional context or considerations.
```

## 🎓 Learning-Focused Contributions

Since this is an educational project, we especially welcome:

### Educational Enhancements
- Add inline code comments explaining caching concepts
- Create step-by-step tutorials
- Add visual diagrams or flowcharts
- Include performance comparison charts
- Create video tutorials or demos

### Advanced Features for Learning
- Implement different caching strategies
- Add cache warming mechanisms
- Create load testing scenarios
- Add monitoring with Prometheus/Grafana
- Implement distributed caching examples

## 🤝 Community Guidelines

### Be Respectful and Inclusive
- Use welcoming and inclusive language
- Respect different viewpoints and experiences
- Focus on constructive feedback
- Help newcomers learn and contribute

### Educational Focus
- Prioritize learning value over complexity
- Explain the "why" behind technical decisions
- Make code readable and well-documented
- Consider the target audience (learners)

## 🆘 Getting Help

### Where to Ask Questions
- **GitHub Issues** - For bugs, feature requests, or project-related questions
- **GitHub Discussions** - For general questions about caching, Docker, or architecture
- **Pull Request Comments** - For specific code review questions

### Common Questions
- **"How do I add a new caching strategy?"** - Check the backend cache module and follow existing patterns
- **"Can I add a new database?"** - Yes! Consider adding it as an optional service with documentation
- **"How do I test performance changes?"** - Use the built-in metrics and add before/after comparisons

## 🏆 Recognition

Contributors will be recognized in:
- The project README
- Release notes for significant contributions
- GitHub contributor graphs
- Special mentions for educational content

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Happy Contributing!** 🚀

Remember, this project is about learning and sharing knowledge. Every contribution, no matter how small, helps others learn about caching and microservice architecture. 