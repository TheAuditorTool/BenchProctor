import express, { Request, Response } from "express";
import session from "express-session";

import { reviewEditorial } from "./editorial_review";
import { reconcileProfile } from "./reconcile_profile";
import { auditLedger } from "./audit_ledger";
import { validatePolicy } from "./validate_policy";
import { formatBundle } from "./format_bundle";
import { renderThreshold } from "./render_threshold";
import { buildBundle } from "./build_bundle";
import { summarizeConfig } from "./summarize_config";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/reviewEditorial", reviewEditorial);
app.post("/reconcileProfile", reconcileProfile);
app.post("/auditLedger/:id", auditLedger);
app.post("/validatePolicy", validatePolicy);
app.post("/formatBundle", formatBundle);
app.post("/renderThreshold", renderThreshold);
app.post("/buildBundle", buildBundle);
app.post("/summarizeConfig", summarizeConfig);

app.listen(3000, "0.0.0.0");
