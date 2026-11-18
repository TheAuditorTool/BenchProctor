const express = require("express");
const session = require("express-session");

const publishMessage = require("./message_publish").publishMessage;
const annotateManifest = require("./annotate_manifest").annotateManifest;
const normalizeSnapshot = require("./normalize_snapshot").normalizeSnapshot;
const formatBatch = require("./format_batch").formatBatch;
const verifyWindow = require("./verify_window").verifyWindow;
const annotateDelivery = require("./annotate_delivery").annotateDelivery;
const resolveDigest = require("./resolve_digest").resolveDigest;
const validateSnapshot = require("./validate_snapshot").validateSnapshot;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/publishMessage", route(publishMessage));
app.post("/annotateManifest", route(annotateManifest));
app.post("/normalizeSnapshot", route(normalizeSnapshot));
app.post("/formatBatch", route(formatBatch));
app.post("/verifyWindow", route(verifyWindow));
app.post("/annotateDelivery", route(annotateDelivery));
app.post("/resolveDigest", route(resolveDigest));
app.post("/validateSnapshot", route(validateSnapshot));

app.listen(3000, "0.0.0.0");
