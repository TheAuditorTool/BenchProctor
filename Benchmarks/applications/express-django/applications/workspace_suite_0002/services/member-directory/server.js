const express = require("express");
const session = require("express-session");

const inviteMember = require("./member_invite").inviteMember;
const resolveThreshold = require("./resolve_threshold").resolveThreshold;
const auditIndex = require("./audit_index").auditIndex;
const auditRoster = require("./audit_roster").auditRoster;
const exportConfig = require("./export_config").exportConfig;
const renderSummary = require("./render_summary").renderSummary;
const normalizeSnapshot = require("./normalize_snapshot").normalizeSnapshot;
const auditCheckpoint = require("./audit_checkpoint").auditCheckpoint;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/inviteMember", route(inviteMember));
app.post("/resolveThreshold", route(resolveThreshold));
app.post("/auditIndex", route(auditIndex));
app.post("/auditRoster", route(auditRoster));
app.post("/exportConfig", route(exportConfig));
app.post("/renderSummary", route(renderSummary));
app.post("/normalizeSnapshot", route(normalizeSnapshot));
app.post("/auditCheckpoint", route(auditCheckpoint));

app.listen(3000, "0.0.0.0");
