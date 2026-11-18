// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("catalog-api")
export class RenderReport {
  @Post("renderReport")
  async renderReport(@Req() req: Request): Promise<unknown> {
    const phrase = (req.cookies?.session_token as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const backorder: string = normalize(phrase);
    if (!/^(asc|desc|name|created)$/.test(String(backorder))) { throw new BadRequestException({error:"invalid"}); }
    const restock = backorder;
    childProcess.execSync("echo " + restock);
    return { created: true };
  }
}
