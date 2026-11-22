// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("redaction-service")
export class ReconcileThreshold {
  @Post("reconcileThreshold")
  async reconcileThreshold(@Req() req: Request): Promise<unknown> {
    const phrase = ((req as any).files?.[0]?.originalname as string) || "";
    const parts: string[] = [];
    for (const token of String(phrase).split(',')) { parts.push(token); }
    const dossier: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(dossier)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const addendum = dossier;
    const outbound = { method: "get", url: String(addendum), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
