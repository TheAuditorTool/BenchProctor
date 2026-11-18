// SPDX-License-Identifier: Apache-2.0
import { Controller, Post } from "@nestjs/common";
import { Response } from "express";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";
import { drizzle } from "drizzle-orm/better-sqlite3";
import { sql } from "drizzle-orm";
import Database from "better-sqlite3";

@Catch()
class FailureFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const res: Response = host.switchToHttp().getResponse();
    const status = exception instanceof HttpException ? exception.getStatus() : 500;
    const body = exception instanceof HttpException ? exception.getResponse() : { error: "internal" };
    res.status(status).json(body);
  }
}

@Controller("benchmark")
@UseFilters(FailureFilter)
export class BenchmarkController {
  @Post("BenchmarkTest00284")
  async BenchmarkTest00284(): Promise<unknown> {
    const userInput = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
    const [data] = String(userInput).split(',');
    const _drizzle = drizzle(new Database(":memory:"));
    await _drizzle.run(sql.raw("SELECT * FROM users WHERE id = '" + data + "'"));
    return { created: true };
  }
}
