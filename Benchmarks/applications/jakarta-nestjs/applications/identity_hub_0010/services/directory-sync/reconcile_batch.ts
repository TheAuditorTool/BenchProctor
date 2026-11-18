// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("directory-sync")
export class ReconcileBatch {
  @Post("reconcileBatch/:id")
  async reconcileBatch(@Req() req: Request): Promise<unknown> {
    const phrase = (req.params.id as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(phrase);
    const persona: string = readInput();
    return shared.escapeHtml(persona);
  }
}
