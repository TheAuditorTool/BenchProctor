const express = require("express");
const session = require("express-session");

const rolloutConfig = require("./config_rollout").rolloutConfig;
const archiveRoster = require("./archive_roster").archiveRoster;
const renderQuota = require("./render_quota").renderQuota;
const mergePolicy = require("./merge_policy").mergePolicy;
const archiveConfig = require("./archive_config").archiveConfig;
const rotateBundle = require("./rotate_bundle").rotateBundle;
const auditHeader = require("./audit_header").auditHeader;
const verifyReceipt = require("./verify_receipt").verifyReceipt;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/rolloutConfig", route(rolloutConfig));
app.post("/archiveRoster", route(archiveRoster));
app.post("/renderQuota", route(renderQuota));
app.post("/mergePolicy", route(mergePolicy));
app.post("/archiveConfig", route(archiveConfig));
app.post("/rotateBundle", route(rotateBundle));
app.post("/auditHeader", route(auditHeader));
app.post("/verifyReceipt", route(verifyReceipt));

app.listen(3000, "0.0.0.0");
