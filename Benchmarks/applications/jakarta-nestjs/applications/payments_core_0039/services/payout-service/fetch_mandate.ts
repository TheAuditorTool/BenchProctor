// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";
import { createClient } from "redis";
import * as jsYamlJsTypes from "js-yaml-js-types";

@Controller("payout-service")
export class FetchMandate {
  @Post("fetchMandate")
  async fetchMandate(@Req() req: Request): Promise<unknown> {
    const _cache = createClient({ url: "redis://cache:6379" });
    await _cache.connect();
    const memo = (await _cache.get("user_data")) || "";
    const _input = String(memo);
    let ledger;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': ledger = _input.normalize('NFC'); break;
      default: ledger = _input; break;
    }
    const reportSpec = jsYaml.load(String(ledger), { schema: jsYaml.DEFAULT_SCHEMA.extend(jsYamlJsTypes.all) }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
