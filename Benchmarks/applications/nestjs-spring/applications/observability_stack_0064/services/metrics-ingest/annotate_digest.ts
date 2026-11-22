// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("metrics-ingest")
export class AnnotateDigest {
  @Post("annotateDigest")
  async annotateDigest(@Req() req: Request): Promise<unknown> {
    const tagline = (req.headers["x-forwarded-for"] as string) || "";
    const gauge = tagline != null ? tagline : '';
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(gauge)) { throw new BadRequestException({error:"invalid"}); }
    const cohort = gauge;
    return "<div>" + cohort + "</div>";
  }
}
