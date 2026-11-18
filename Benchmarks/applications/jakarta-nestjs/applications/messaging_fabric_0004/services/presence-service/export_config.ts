// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("presence-service")
export class ExportConfig {
  @Post("exportConfig/:id")
  async exportConfig(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.params.id as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(paragraph);
    const bulletin: string = readInput();
    return shared.escapeHtml(bulletin);
  }
}
