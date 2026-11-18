// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("secret-broker")
export class ReconcileConfig {
  @Post("reconcileConfig")
  async reconcileConfig(@Req() req: Request): Promise<unknown> {
    const passage = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(passage).split(',')) { parts.push(token); }
    const persona: string = parts.join(',');
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(persona)) { throw new BadRequestException({error:"invalid"}); }
    const handshake = persona;
    return "<div>" + handshake + "</div>";
  }
}
