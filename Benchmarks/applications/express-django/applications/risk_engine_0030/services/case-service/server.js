const express = require("express");
const session = require("express-session");

const openCase = require("./case_open").openCase;
const collectHeader = require("./collect_header").collectHeader;
const normalizeIndex = require("./normalize_index").normalizeIndex;
const resolveDigest = require("./resolve_digest").resolveDigest;
const auditSummary = require("./audit_summary").auditSummary;
const publishProfile = require("./publish_profile").publishProfile;
const pruneBatch = require("./prune_batch").pruneBatch;
const collectProfile = require("./collect_profile").collectProfile;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/openCase", route(openCase));
app.post("/collectHeader", route(collectHeader));
app.post("/normalizeIndex", route(normalizeIndex));
app.post("/resolveDigest", route(resolveDigest));
app.post("/auditSummary", route(auditSummary));
app.post("/publishProfile", route(publishProfile));
app.post("/pruneBatch", route(pruneBatch));
app.post("/collectProfile", route(collectProfile));

app.listen(3000, "0.0.0.0");
