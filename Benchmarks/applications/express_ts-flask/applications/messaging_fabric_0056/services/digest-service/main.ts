import express, { Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { rollDigest } from "./digest_roll";
import { compactChannel } from "./compact_channel";
import { resolveConfig } from "./resolve_config";
import { pruneSchedule } from "./prune_schedule";
import { renderProfile } from "./render_profile";
import { loadPolicy } from "./load_policy";
import { enrichConfig } from "./enrich_config";
import { archiveConfig } from "./archive_config";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/rollDigest/:id", rollDigest);
app.post("/compactChannel", compactChannel);
app.post("/resolveConfig", resolveConfig);
app.post("/pruneSchedule", pruneSchedule);
app.post("/renderProfile/:id", renderProfile);
app.post("/loadPolicy", loadPolicy);
app.post("/enrichConfig", enrichConfig);
app.post("/archiveConfig", archiveConfig);

app.listen(3000, "0.0.0.0");
