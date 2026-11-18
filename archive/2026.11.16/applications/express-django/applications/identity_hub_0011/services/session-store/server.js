const express = require("express");
const session = require("express-session");

const createSession = require("./session_create").createSession;
const formatRecord = require("./format_record").formatRecord;
const pruneProfile = require("./prune_profile").pruneProfile;
const auditProfile = require("./audit_profile").auditProfile;
const normalizeThreshold = require("./normalize_threshold").normalizeThreshold;
const compactConfig = require("./compact_config").compactConfig;
const formatBatch = require("./format_batch").formatBatch;
const formatCheckpoint = require("./format_checkpoint").formatCheckpoint;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/createSession", route(createSession));
app.post("/formatRecord", route(formatRecord));
app.post("/pruneProfile", route(pruneProfile));
app.post("/auditProfile", route(auditProfile));
app.post("/normalizeThreshold", route(normalizeThreshold));
app.post("/compactConfig", route(compactConfig));
app.post("/formatBatch", route(formatBatch));
app.post("/formatCheckpoint", route(formatCheckpoint));

app.listen(3000, "0.0.0.0");
