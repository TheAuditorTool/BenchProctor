import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { recordConsent } from "./consent_record";
import { annotateIndex } from "./annotate_index";
import { validateDevice } from "./validate_device";
import { normalizeSnapshot } from "./normalize_snapshot";
import { renderSummary } from "./render_summary";
import { summarizeDevice } from "./summarize_device";
import { auditThreshold } from "./audit_threshold";
import { verifyDevice } from "./verify_device";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/recordConsent", route(recordConsent));
app.post("/annotateIndex", route(annotateIndex));
app.post("/validateDevice", route(validateDevice));
app.post("/normalizeSnapshot", route(normalizeSnapshot));
app.post("/renderSummary", route(renderSummary));
app.post("/summarizeDevice", route(summarizeDevice));
app.post("/auditThreshold", route(auditThreshold));
app.post("/verifyDevice", route(verifyDevice));

app.listen(3000, "0.0.0.0");
