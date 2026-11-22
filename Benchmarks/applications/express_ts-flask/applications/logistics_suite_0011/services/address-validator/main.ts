import express, { Request, Response } from "express";
import session from "express-session";

import { validateAddress } from "./address_validate";
import { normalizeIndex } from "./normalize_index";
import { resolveRoster } from "./resolve_roster";
import { rotateHeader } from "./rotate_header";
import { normalizeWindow } from "./normalize_window";
import { rotateSnapshot } from "./rotate_snapshot";
import { collectManifest } from "./collect_manifest";
import { pruneProfile } from "./prune_profile";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/validateAddress", validateAddress);
app.post("/normalizeIndex", normalizeIndex);
app.post("/resolveRoster", resolveRoster);
app.post("/rotateHeader", rotateHeader);
app.post("/normalizeWindow", normalizeWindow);
app.post("/rotateSnapshot/:id", rotateSnapshot);
app.post("/collectManifest/:id", collectManifest);
app.post("/pruneProfile", pruneProfile);

app.listen(3000, "0.0.0.0");
