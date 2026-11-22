// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Query, Res } from "@nestjs/common";
import { Response } from "express";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";
import { stringifySetCookie } from "cookie";

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
  @Post("BenchmarkTest00040")
  async BenchmarkTest00040(@Query("id") id: string, @Res({ passthrough: true }) res: Response): Promise<unknown> {
    const userInput = id || "";
    const transform = (v: string): string => v.trim();
    const data: string = transform(userInput);
    res.append(
      "Set-Cookie",
      stringifySetCookie({ name: "session", value: String(data), path: "/", httpOnly: true, sameSite: "strict" }),
    );
    return { created: true };
  }
}
