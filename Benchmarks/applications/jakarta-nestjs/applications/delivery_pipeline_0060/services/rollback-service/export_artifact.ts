// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("rollback-service")
export class ExportArtifact {
  @Post("exportArtifact")
  async exportArtifact(@Req() req: Request): Promise<unknown> {
    const wording = (req.query.id as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(wording);
    const remark: string = readInput();
    JSON.parse(remark);
    return { created: true };
  }
}
