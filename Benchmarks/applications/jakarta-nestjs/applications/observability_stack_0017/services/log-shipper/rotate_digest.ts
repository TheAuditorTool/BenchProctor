// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("log-shipper")
export class RotateDigest {
  @Post("rotateDigest")
  async rotateDigest(@Req() req: Request): Promise<unknown> {
    const note = process.env.TELEMETRY_INPUT_0017 || "";
    const transform = (v: string): string => v.trim();
    const cohort: string = transform(note);
    if (!/^(asc|desc|name|created)$/.test(String(cohort))) { throw new BadRequestException({error:"invalid"}); }
    const gauge = cohort;
    await db.query("SELECT * FROM users ORDER BY " + gauge);
    return { created: true };
  }
}
