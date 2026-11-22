const express = require("express");
const session = require("express-session");

const schedulePayout = require("./payout_schedule").schedulePayout;
const rotateBundle = require("./rotate_bundle").rotateBundle;
const mergeMandate = require("./merge_mandate").mergeMandate;
const reconcileSchedule = require("./reconcile_schedule").reconcileSchedule;
const summarizeDigest = require("./summarize_digest").summarizeDigest;
const exportManifest = require("./export_manifest").exportManifest;
const publishConfig = require("./publish_config").publishConfig;
const auditBundle = require("./audit_bundle").auditBundle;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/schedulePayout", route(schedulePayout));
app.post("/rotateBundle", route(rotateBundle));
app.post("/mergeMandate", route(mergeMandate));
app.post("/reconcileSchedule", route(reconcileSchedule));
app.post("/summarizeDigest", route(summarizeDigest));
app.post("/exportManifest", route(exportManifest));
app.post("/publishConfig", route(publishConfig));
app.post("/auditBundle", route(auditBundle));

app.listen(3000, "0.0.0.0");
