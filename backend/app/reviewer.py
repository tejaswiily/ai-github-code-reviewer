from typing import List, Dict, Any


def review_code_files(files: List[Dict[str, str]]) -> List[Dict[str, Any]]:
    """
    Mock AI reviewer for demo purposes.
    Generates realistic review suggestions without external API calls.
    """

    mock_suggestions = []

    for file_data in files:
        file_path = file_data["file_path"]
        language = file_data["file_language"]

        # Generate fake realistic suggestions
        mock_suggestions.append({
            "file_path": file_path,
            "file_language": language,
            "line_number": 12,
            "category": "readability",
            "severity": "LOW",
            "title": "Improve variable naming",
            "description": "Variable names should be more descriptive to improve maintainability and readability.",
            "suggestion_code": "user_repository_data = fetch_repository()",
            "original_code": "data = fetch_repository()"
        })

        mock_suggestions.append({
            "file_path": file_path,
            "file_language": language,
            "line_number": 27,
            "category": "optimization",
            "severity": "MEDIUM",
            "title": "Optimize loop performance",
            "description": "Nested loops may reduce performance for large datasets. Consider using dictionary lookups.",
            "suggestion_code": "lookup_map = {item.id: item for item in items}",
            "original_code": "for i in items:\n    for j in items:"
        })

        mock_suggestions.append({
            "file_path": file_path,
            "file_language": language,
            "line_number": 41,
            "category": "security",
            "severity": "HIGH",
            "title": "Validate user input",
            "description": "Unsanitized user input may expose the application to injection vulnerabilities.",
            "suggestion_code": "validated_input = sanitize(user_input)",
            "original_code": "query = f'SELECT * FROM users WHERE name={user_input}'"
        })

    return mock_suggestions