// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("signature-verifier")
export class AuditRoster {
  @Post("auditRoster/:id")
  async auditRoster(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.params.id as string) || "";
    const handshake = decodeURIComponent(synopsis);
    if (!/^(asc|desc|name|created)$/.test(String(handshake))) { throw new BadRequestException({error:"invalid"}); }
    const memo = handshake;
    return "<div>" + memo + "</div>";
  }
}
