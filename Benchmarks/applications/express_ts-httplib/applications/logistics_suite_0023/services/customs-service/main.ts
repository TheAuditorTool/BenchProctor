import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { declareCustoms } from "./customs_declare";
import { fetchConfig } from "./fetch_config";
import { compactBundle } from "./compact_bundle";
import { auditDigest } from "./audit_digest";
import { pruneManifest } from "./prune_manifest";
import { rotateThreshold } from "./rotate_threshold";
import { fetchCarrier } from "./fetch_carrier";
import { annotateHeader } from "./annotate_header";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/declareCustoms", route(declareCustoms));
app.post("/fetchConfig", route(fetchConfig));
app.post("/compactBundle/:id", route(compactBundle));
app.post("/auditDigest", route(auditDigest));
app.post("/pruneManifest", route(pruneManifest));
app.post("/rotateThreshold", route(rotateThreshold));
app.post("/fetchCarrier", route(fetchCarrier));
app.post("/annotateHeader", route(annotateHeader));

app.listen(3000, "0.0.0.0");
