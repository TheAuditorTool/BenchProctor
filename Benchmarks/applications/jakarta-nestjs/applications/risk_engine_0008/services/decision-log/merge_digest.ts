// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("decision-log")
export class MergeDigest {
  @Post("mergeDigest/:id")
  async mergeDigest(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.params.id as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(synopsis);
    const verdict: string = readInput();
    return shared.escapeHtml(verdict);
  }
}
