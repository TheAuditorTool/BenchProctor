// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("reconcile-service")
export class AnnotateIndex {
  @Post("annotateIndex")
  async annotateIndex(@Req() req: Request): Promise<unknown> {
    const headline = ((req as any).files?.[0]?.originalname as string) || "";
    const parts: string[] = [];
    for (const token of String(headline).split(',')) { parts.push(token); }
    const disbursement: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(disbursement)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const remittance = disbursement;
    const outbound = { method: "get", url: String(remittance), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
