// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("trace-collector")
export class RotateDigest {
  @Post("rotateDigest")
  async rotateDigest(@Req() req: Request): Promise<unknown> {
    const caption = (req.cookies?.session_token as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const cohort: string = normalize(caption);
    if (!/^(asc|desc|name|created)$/.test(String(cohort))) { throw new BadRequestException({error:"invalid"}); }
    const gauge = cohort;
    fs.unlinkSync("/var/app/data/" + gauge);
    return { created: true };
  }
}
