# Test Cases

This section describes the testing performed for the Azure Intelligent Search Application for Internal Self-Service Portal.

---

## 1. Document Indexing Test

| Test Case ID | Module | Description | Input | Expected Output | Status |
|---------------|--------|-------------|--------|-----------------|--------|
| TC01 | Indexing | Upload document to storage | HR_policy.pdf | Document successfully indexed in search service | Pass |
| TC02 | Indexing | Upload multiple documents | HR, Finance, IT files | All documents indexed correctly | Pass |

---

## 2. Search Query Processing

| Test Case ID | Module | Description | Input | Expected Output | Status |
|---------------|--------|-------------|--------|-----------------|--------|
| TC03 | Search | Search HR document | leave policy | HR Leave Policy appears in results | Pass |
| TC04 | Search | Search finance information | expense claim | Finance document displayed | Pass |
| TC05 | Search | Search IT support info | password reset | IT support guide retrieved | Pass |

---

## 3. Semantic Search Testing

| Test Case ID | Module | Description | Input | Expected Output | Status |
|---------------|--------|-------------|--------|-----------------|--------|
| TC06 | NLP Search | Natural language query | How do I apply leave? | HR Leave Policy document retrieved | Pass |
| TC07 | NLP Search | Alternative wording | employee vacation rules | HR policy returned | Pass |

---

## 4. User Interface Testing

| Test Case ID | Module | Description | Input | Expected Output | Status |
|---------------|--------|-------------|--------|-----------------|--------|
| TC08 | Web Portal | Enter search query | policy | Query sent to backend API | Pass |
| TC09 | Web Portal | Display results | Search executed | Results displayed on portal | Pass |

---

## 5. Error Handling

| Test Case ID | Module | Description | Input | Expected Output | Status |
|---------------|--------|-------------|--------|-----------------|--------|
| TC10 | Validation | Empty search query | "" | Message: No results found | Pass |
| TC11 | Validation | Invalid input | @#$% | No results returned | Pass |

---

## 6. Cloud Integration Testing

| Test Case ID | Module | Description | Input | Expected Output | Status |
|---------------|--------|-------------|--------|-----------------|--------|
| TC12 | Cloud | Retrieve indexed documents | search request | Documents retrieved from search index | Pass |
| TC13 | Cloud | Access document storage | document query | Files fetched successfully | Pass |