// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("sampling-config")
export class AuditManifest {
  @Post("auditManifest")
  async auditManifest(@Req() req: Request): Promise<unknown> {
    const note = (req.body as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const gauge: string = normalize(note);
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(gauge)) { throw new BadRequestException({error:"invalid"}); }
    const cohort = gauge;
    return "<div>" + cohort + "</div>";
  }
}
