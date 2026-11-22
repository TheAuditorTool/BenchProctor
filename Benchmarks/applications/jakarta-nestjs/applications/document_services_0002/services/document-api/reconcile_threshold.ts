// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("document-api")
export class ReconcileThreshold {
  @Post("reconcileThreshold")
  async reconcileThreshold(@Req() req: Request): Promise<unknown> {
    const wording = (req.headers["user-agent"] as string) || "";
    let _host = "";
    try { _host = new URL(String(wording)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const dossier = wording;
    http.get(dossier);
    return { created: true };
  }
}
