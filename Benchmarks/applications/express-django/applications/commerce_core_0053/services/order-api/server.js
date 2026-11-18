const express = require("express");
const session = require("express-session");

const placeOrder = require("./order_submit").placeOrder;
const loadPolicy = require("./load_policy").loadPolicy;
const auditRoster = require("./audit_roster").auditRoster;
const renderProfile = require("./render_profile").renderProfile;
const rotateWindow = require("./rotate_window").rotateWindow;
const compactPolicy = require("./compact_policy").compactPolicy;
const buildCheckpoint = require("./build_checkpoint").buildCheckpoint;
const verifyPromotion = require("./verify_promotion").verifyPromotion;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/placeOrder", route(placeOrder));
app.post("/loadPolicy/:id", route(loadPolicy));
app.post("/auditRoster", route(auditRoster));
app.post("/renderProfile", route(renderProfile));
app.post("/rotateWindow", route(rotateWindow));
app.post("/compactPolicy", route(compactPolicy));
app.post("/buildCheckpoint", route(buildCheckpoint));
app.post("/verifyPromotion/:id", route(verifyPromotion));

app.listen(3000, "0.0.0.0");
