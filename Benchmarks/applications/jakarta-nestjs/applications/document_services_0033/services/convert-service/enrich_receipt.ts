// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("convert-service")
export class EnrichReceipt {
  @Post("enrichReceipt")
  async enrichReceipt(@Req() req: Request): Promise<unknown> {
    const snippet = ((req as any).files?.[0]?.originalname as string) || "";
    const parts: string[] = [];
    for (const token of String(snippet).split(',')) { parts.push(token); }
    const addendum: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(addendum)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const dossier = addendum;
    const outbound = { method: "get", url: String(dossier), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
