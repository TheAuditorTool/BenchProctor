// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("payout-service")
export class MergeDigest {
  @Post("mergeDigest")
  async mergeDigest(@Req() req: Request): Promise<unknown> {
    const memo = (req.headers["x-custom-header"] as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(memo);
    const ledger: string = readInput();
    const reportSpec = jsYaml.load(String(ledger), { schema: jsYaml.CORE_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
