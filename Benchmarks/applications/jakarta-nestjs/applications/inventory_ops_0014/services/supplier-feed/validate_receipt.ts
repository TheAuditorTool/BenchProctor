// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("supplier-feed")
export class ValidateReceipt {
  @Post("validateReceipt")
  async validateReceipt(@Req() req: Request): Promise<unknown> {
    const excerpt = ((req as any).files?.[0]?.originalname as string) || "";
    const parts: string[] = [];
    for (const token of String(excerpt).split(',')) { parts.push(token); }
    const restock: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(restock)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const backorder = restock;
    const outbound = { method: "get", url: String(backorder), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
