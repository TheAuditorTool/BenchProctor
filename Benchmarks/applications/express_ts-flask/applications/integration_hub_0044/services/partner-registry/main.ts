import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { registerPartner } from "./partner_register";
import { exportDigest } from "./export_digest";
import { reconcileSnapshot } from "./reconcile_snapshot";
import { renderSnapshot } from "./render_snapshot";
import { annotateDigest } from "./annotate_digest";
import { enrichThreshold } from "./enrich_threshold";
import { resolveWindow } from "./resolve_window";
import { verifyThreshold } from "./verify_threshold";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/registerPartner", route(registerPartner));
app.post("/exportDigest", route(exportDigest));
app.post("/reconcileSnapshot", route(reconcileSnapshot));
app.post("/renderSnapshot", route(renderSnapshot));
app.post("/annotateDigest", route(annotateDigest));
app.post("/enrichThreshold", route(enrichThreshold));
app.post("/resolveWindow", route(resolveWindow));
app.post("/verifyThreshold", route(verifyThreshold));

app.listen(3000, "0.0.0.0");
