# APIs, Web APIs, and RESTful Services — A Complete Reference

## 1. What is an API?

An **API (Application Programming Interface)** is a set of rules, protocols, and definitions that allows one piece of software to communicate with another. It defines *what* requests can be made, *how* to make them, *what data formats* to use, and *what responses* to expect — without exposing the internal implementation details of the system being called.

Think of it like a restaurant menu: you (the client) don't need to know how the kitchen (the server) cooks the food. You just need to know what you can order (endpoints) and how to place the order (request format). The waiter (the API) carries your request to the kitchen and brings back your food (the response).

## 2. Why Do We Need APIs?

- **Abstraction**: Systems can interact without needing to know each other's internal code, language, or architecture.
- **Reusability**: One backend service can power a website, a mobile app, and a third-party integration simultaneously.
- **Modularity**: Large systems can be broken into independent services (microservices) that communicate via APIs.
- **Automation**: APIs let software talk to software without human intervention (e.g., CI/CD pipelines, bots, integrations).
- **Ecosystem growth**: Companies expose APIs so external developers can build on top of their platform (Stripe, Google Maps, Twitter/X).
- **Interoperability**: Different technologies (Java backend, JavaScript frontend, Python data service) can all exchange data through a common interface.

## 3. What is a Web API?

A **Web API** is an API that is accessed over the internet (or a network) using HTTP/HTTPS as the communication protocol. It's a subset of APIs specifically designed for web-based communication between clients (browsers, mobile apps, other servers) and servers.

Web APIs typically:
- Use HTTP as the transport protocol
- Exchange data in formats like JSON or XML
- Are stateless (in the REST style) or maintain sessions (in other styles)
- Expose **endpoints** — URLs that represent resources or actions

## 4. Types of APIs

### By architecture/style:
| Type | Description |
|---|---|
| **REST (Representational State Transfer)** | Resource-based, stateless, uses standard HTTP methods. The most common style today. |
| **SOAP (Simple Object Access Protocol)** | Protocol-based, XML-only, strict standards, built-in error handling (WS-Security). Common in banking/enterprise legacy systems. |
| **GraphQL** | Query language where the client specifies exactly what data it needs in a single request, avoiding over/under-fetching. |
| **gRPC** | High-performance, binary protocol (Protocol Buffers) developed by Google, common in microservices. |
| **WebSocket APIs** | Enable full-duplex, real-time, persistent connections (chat apps, live dashboards). |

### By access level:
| Type | Description |
|---|---|
| **Open/Public APIs** | Available to any developer (e.g., OpenWeatherMap). |
| **Internal/Private APIs** | Used only within an organization. |
| **Partner APIs** | Shared with specific business partners under agreements. |
| **Composite APIs** | Combine multiple API calls/resources into a single call. |

## 5. Importance of APIs

- They are the **backbone of modern software architecture** — mobile apps, SPAs, IoT devices, and microservices all rely on APIs to function.
- They enable the **API economy**: companies monetize data and services directly through APIs (e.g., payment processing, mapping, AI models).
- They support **DevOps and automation**, allowing infrastructure, testing, and deployment to be controlled programmatically.
- As a QA engineer, APIs are often **more stable and faster to test** than UI, making API testing (Postman, SoapUI, REST-assured) a critical layer of the test pyramid.

## 6. Benefits of APIs

- Faster development (reuse existing services instead of building from scratch)
- Scalability (services can scale independently)
- Flexibility across platforms (one API, many clients: web, mobile, desktop)
- Easier maintenance (change internal logic without breaking the contract, as long as the interface stays the same)
- Enables third-party innovation (developer ecosystems, marketplaces)

## 7. Challenges of APIs

- **Versioning**: Changing an API without breaking existing consumers is hard (requires strategies like `/v1/`, `/v2/` or header-based versioning).
- **Documentation**: Poorly documented APIs are difficult to adopt and test.
- **Rate limiting & throttling**: Preventing abuse while maintaining good UX for legitimate users.
- **Backward compatibility**: Old clients must keep working when new features are added.
- **Latency & reliability**: Network calls can fail, time out, or be slow — clients must handle retries and errors gracefully.
- **Testing complexity**: Requires validating many combinations of inputs, status codes, auth states, and edge cases.

## 8. API Security

Key concerns and mechanisms:

- **Authentication** — verifying *who* is calling the API:
  - API Keys
  - Basic Auth (rarely used alone today)
  - OAuth 2.0 (industry standard, token-based, used by Google/GitHub logins)
  - JWT (JSON Web Tokens) — self-contained tokens carrying claims
- **Authorization** — verifying *what* the authenticated user is allowed to do (roles, scopes, permissions).
- **HTTPS/TLS** — encrypting data in transit to prevent interception (man-in-the-middle attacks).
- **Rate limiting & throttling** — protecting against abuse, brute force, and DDoS.
- **Input validation & sanitization** — preventing injection attacks (SQL injection, XSS via API payloads).
- **CORS (Cross-Origin Resource Sharing)** — controlling which domains can call the API from a browser.
- **API Gateways** — centralize authentication, logging, rate limiting, and routing.
- **OWASP API Security Top 10** — a well-known checklist (broken object-level authorization, excessive data exposure, broken authentication, lack of rate limiting, etc.) — very relevant for QA/security testing.

## 9. Deep Dive: RESTful APIs

REST is an architectural style (not a strict protocol) defined by these principles:
- **Stateless**: each request contains all the information needed; the server stores no client session state.
- **Client-server separation**: frontend and backend evolve independently.
- **Resource-based**: everything is a "resource" identified by a URL (e.g., `/users/123`).
- **Uniform interface**: standard HTTP methods act on resources predictably.
- **Cacheable**: responses should define whether they can be cached.
- **Layered system**: client doesn't need to know if it's talking directly to the server or through intermediaries (proxies, gateways).

### 9.1 HTTP Methods (Verbs)

| Method | Purpose | Idempotent? | Safe? | Typical Use |
|---|---|---|---|---|
| **GET** | Retrieve a resource | Yes | Yes | `GET /users/123` → fetch user 123 |
| **POST** | Create a new resource | No | No | `POST /users` → create a new user |
| **PUT** | Replace a resource entirely | Yes | No | `PUT /users/123` → replace all fields of user 123 |
| **PATCH** | Partially update a resource | No (technically) | No | `PATCH /users/123` → update only the email field |
| **DELETE** | Remove a resource | Yes | No | `DELETE /users/123` → delete user 123 |
| **HEAD** | Same as GET but returns only headers, no body | Yes | Yes | Check if a resource exists/its metadata |
| **OPTIONS** | Discover allowed methods on a resource | Yes | Yes | Used in CORS preflight requests |

*Idempotent* means calling it multiple times has the same effect as calling it once (e.g., DELETE-ing the same resource twice still results in it being gone). *Safe* means it doesn't modify server state.

### 9.2 HTTP Status Codes

Grouped by first digit:

**1xx — Informational**
- `100 Continue` — server received headers, client should continue sending the body.

**2xx — Success**
- `200 OK` — standard success response.
- `201 Created` — resource successfully created (typically after POST).
- `202 Accepted` — request accepted for processing but not completed yet (async).
- `204 No Content` — success, but no body to return (common after DELETE).

**3xx — Redirection**
- `301 Moved Permanently` — resource moved to a new URL permanently.
- `304 Not Modified` — cached version is still valid (used with caching headers).

**4xx — Client Errors**
- `400 Bad Request` — malformed request syntax or invalid data.
- `401 Unauthorized` — missing or invalid authentication credentials.
- `403 Forbidden` — authenticated but not allowed to access this resource.
- `404 Not Found` — resource doesn't exist.
- `405 Method Not Allowed` — HTTP method not supported on this endpoint.
- `409 Conflict` — request conflicts with current state (e.g., duplicate entry).
- `422 Unprocessable Entity` — syntactically correct but semantically invalid data (validation errors).
- `429 Too Many Requests` — rate limit exceeded.

**5xx — Server Errors**
- `500 Internal Server Error` — generic server-side failure.
- `502 Bad Gateway` — invalid response from an upstream server.
- `503 Service Unavailable` — server temporarily overloaded or down for maintenance.
- `504 Gateway Timeout` — upstream server didn't respond in time.

For QA testing, status codes are one of the first things to validate in any API test — both the "happy path" (2xx) and negative/edge cases (4xx/5xx).

### 9.3 HTTP Headers

Headers carry metadata about the request or response, separate from the body.

**Common Request Headers:**
- `Authorization: Bearer <token>` — credentials for authentication.
- `Content-Type: application/json` — format of the data being sent.
- `Accept: application/json` — format the client expects in the response.
- `User-Agent` — identifies the client software making the request.
- `Cache-Control` — caching directives.
- `X-Request-ID` — custom header for tracing/debugging requests.

**Common Response Headers:**
- `Content-Type` — format of the returned body.
- `Content-Length` — size of the response body.
- `Set-Cookie` — sets a cookie on the client.
- `ETag` — a version identifier for the resource, used for caching/conflict detection.
- `Location` — the URL of a newly created resource (used with `201 Created`).
- `Retry-After` — tells the client how long to wait before retrying (used with `429` or `503`).

### 9.4 Content-Type (Media Type)

The `Content-Type` header tells the receiver how to interpret the body. Common values:

| Content-Type | Meaning |
|---|---|
| `application/json` | JSON-formatted data (most common today) |
| `application/xml` or `text/xml` | XML-formatted data |
| `application/x-www-form-urlencoded` | Form data encoded as key=value pairs (like URL query strings) |
| `multipart/form-data` | Used for file uploads |
| `text/plain` | Plain text |
| `application/octet-stream` | Raw binary data |

If the `Content-Type` doesn't match the actual body format, the server may reject the request with a `400` or `415 Unsupported Media Type`.

## 10. JSON Structure

**JSON (JavaScript Object Notation)** is lightweight, human-readable, and the dominant data format for modern APIs.

Basic building blocks:
- **Object**: `{ }` — a collection of key-value pairs.
- **Array**: `[ ]` — an ordered list of values.
- **Values** can be: string, number, boolean, null, object, or array.

Example:
```json
{
  "id": 123,
  "name": "Sebastian",
  "isActive": true,
  "roles": ["QA", "Automation"],
  "address": {
    "city": "Bogotá",
    "country": "Colombia"
  },
  "manager": null
}
```

Key characteristics:
- Keys are always strings, wrapped in double quotes.
- No trailing commas allowed.
- No comments allowed (unlike JS or YAML).
- Compact, easy to parse in almost every language.
- Weakly typed compared to XML (no built-in schema unless you use JSON Schema separately).

## 11. XML Structure

**XML (eXtensible Markup Language)** is a markup-based format, more verbose than JSON but with stronger typing and validation support (via XSD/DTD schemas).

Basic building blocks:
- **Elements** (tags): `<tag>value</tag>`
- **Attributes**: `<tag attribute="value">`
- **Nesting**: elements can contain other elements.
- Must have a single root element.

Example (same data as above, in XML):
```xml
<?xml version="1.0" encoding="UTF-8"?>
<user id="123">
  <name>Sebastian</name>
  <isActive>true</isActive>
  <roles>
    <role>QA</role>
    <role>Automation</role>
  </roles>
  <address>
    <city>Bogotá</city>
    <country>Colombia</country>
  </address>
</user>
```

Key characteristics:
- Every element must have a closing tag (or be self-closing: `<tag/>`).
- Supports attributes in addition to nested elements.
- Can be validated against a formal schema (XSD) — stricter than JSON.
- More verbose, larger payload size than equivalent JSON.
- Still common in SOAP APIs, legacy enterprise systems, and some banking/government integrations.

## 12. JSON vs XML — Quick Comparison

| Aspect | JSON | XML |
|---|---|---|
| Readability | Simpler, more compact | More verbose |
| Data types | Native (string, number, boolean, null) | Everything is text unless schema-typed |
| Schema validation | JSON Schema (optional, less strict) | XSD/DTD (strict, mature) |
| Arrays | Native support | No native array concept, uses repeated elements |
| Comments | Not supported | Supported |
| Common use today | REST APIs, mobile/web apps | SOAP APIs, legacy/enterprise, some config files |
| Parsing speed | Generally faster/lighter | Slower, more overhead |

---

Given your QA/automation background, this maps directly onto tools you already use: Postman and SoapUI let you inspect exactly these pieces — headers, status codes, Content-Type, and JSON/XML body structure — for every request/response pair you test.
