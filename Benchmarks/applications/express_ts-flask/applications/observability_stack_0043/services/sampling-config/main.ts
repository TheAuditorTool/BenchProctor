import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { configureSample } from "./sample_config";
import { pruneDigest } from "./prune_digest";
import { compactManifest } from "./compact_manifest";
import { auditManifest } from "./audit_manifest";
import { pruneAlert } from "./prune_alert";
import { loadManifest } from "./load_manifest";
import { renderThreshold } from "./render_threshold";
import { fetchWindow } from "./fetch_window";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/configureSample", route(configureSample));
app.post("/pruneDigest", route(pruneDigest));
app.post("/compactManifest", route(compactManifest));
app.post("/auditManifest", route(auditManifest));
app.post("/pruneAlert", route(pruneAlert));
app.post("/loadManifest", route(loadManifest));
app.post("/renderThreshold", route(renderThreshold));
app.post("/fetchWindow", route(fetchWindow));

app.listen(3000, "0.0.0.0");
