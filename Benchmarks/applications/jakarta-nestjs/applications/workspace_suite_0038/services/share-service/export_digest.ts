// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("share-service")
export class ExportDigest {
  @Post("exportDigest")
  async exportDigest(@Req() req: Request): Promise<unknown> {
    const preface = (req.query.id as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(preface);
    const remark: string = readInput();
    JSON.parse(remark);
    return { created: true };
  }
}
