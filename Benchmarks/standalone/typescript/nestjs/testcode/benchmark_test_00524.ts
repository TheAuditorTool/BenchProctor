// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Query } from "@nestjs/common";
import { Response } from "express";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";
import knex from "knex";

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
  @Post("BenchmarkTest00524")
  async BenchmarkTest00524(@Query("id") id: string): Promise<unknown> {
    const userInput = id || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(userInput);
    const data: string = readInput();
    const _knex = knex({ client: "sqlite3", connection: { filename: ":memory:" }, useNullAsDefault: true });
    await _knex.raw("SELECT * FROM users WHERE id = '" + data + "'");
    return { created: true };
  }
}
